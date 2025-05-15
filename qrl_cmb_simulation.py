from astropy.io import fits
import numpy as np
import pandas as pd
from qiskit import QuantumCircuit, Aer, execute
from qiskit.providers.aer.noise import NoiseModel, depolarizing_error

# Read the FITS file
hdul = fits.open('COM_CMB_IQU-smica-field-Int_2048_R3.00.fits')  # Local path
data = hdul[1].data['I']  # CMB intensity (uK)

# Cycle parameters
cycle_length = 100
window_size = 10
npix = len(data)
indices = np.random.choice(npix, cycle_length, replace=False)
cmb_sample = data[indices]

# Rolling window with dynamic p_error
rewards = []
p_errors = []
delta_ts = []
for i in range(cycle_length - window_size + 1):
    window = cmb_sample[i:i + window_size]
    mean_temp = np.mean(window)
    delta_t = abs(mean_temp - 2.725)
    p_error = min(0.05 + 0.0003 * delta_t, 0.25)  # Adjusted coefficient
    rewards.append(1 if mean_temp > 2.725 + 0.000025 else (-1 if mean_temp < 2.725 - 0.000025 else 0))
    p_errors.append(p_error)
    delta_ts.append(delta_t)

# Statistics
print(f"Cycle: {len(rewards)} days")
print(f"Rewards: +1={rewards.count(1)} ({rewards.count(1)/len(rewards)*100:.1f}%), "
      f"-1={rewards.count(-1)} ({rewards.count(-1)/len(rewards)*100:.1f}%), "
      f"0={rewards.count(0)} ({rewards.count(0)/len(rewards)*100:.1f}%)")

# QRL Circuit
n_qubits = 4
qc = QuantumCircuit(n_qubits, n_qubits)
for qubit in range(n_qubits):
    qc.h(qubit)
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

for i, reward in enumerate(rewards):
    theta = 2.10 + 0.1 * reward
    beta = 1.20 - 0.1 * reward
    qc.rx(theta, i % n_qubits)
    qc.ry(beta, (i + 1) % n_qubits)

qc.rz(np.pi / 2, 2)
qc.measure(range(n_qubits), range(n_qubits))

# Simulation with mean p_error
mean_p_error = np.mean(p_errors)
noise_model = NoiseModel()
error = depolarizing_error(mean_p_error, 1)
noise_model.add_quantum_error(error, ['h', 'cx', 'rx', 'ry', 'rz'])
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024, noise_model=noise_model)
counts = job.result().get_counts(qc)
fidelity = 1 - mean_p_error

# Save results
with open('cmb_results.tex', 'w') as f:
    f.write("\\begin{tabular}{cc}\n\\toprule\nMetric & Value \\\\\n\\midrule\n")
    f.write(f"Cycle Length & {len(rewards)} days \\\\\n")
    f.write(f"Rewards (+1) & {rewards.count(1)} ({rewards.count(1)/len(rewards)*100:.1f}\\%) \\\\\n")
    f.write(f"Rewards (-1) & {rewards.count(-1)} ({rewards.count(-1)/len(rewards)*100:.1f}\%) \\\\\n")
    f.write(f"Rewards (0) & {rewards.count(0)} ({rewards.count(0)/len(rewards)*100:.1f}\%) \\\\\n")
    f.write(f"Fidelity & {fidelity:.1f}\\% \\\\\n")
    f.write("\\bottomrule\n\\end{tabular}")

# Save sorted data for PGFPlots and CSV
data_df = pd.DataFrame({'delta_t': delta_ts, 'p_error': p_errors, 'fidelity': [1-pe for pe in p_errors]})
data_df = data_df.sort_values('delta_t')
data_df.to_csv('p_error.csv', index=False)
data_df[['delta_t', 'fidelity']].to_csv('p_error.dat', sep=' ', index=False, header=False)

with open('counts.dat', 'w') as f:
    for state, count in sorted(counts.items()):
        f.write(f"{state} {count}\n")

hdul.close()
