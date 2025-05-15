# Quantum Trading with Thermal Stability

This project implements a Quantum Reinforcement Learning (QRL) model integrating financial (Bitcoin) and cosmological (CMB) data, achieving high fidelity (~93.7%) under simulated thermal noise. The project is documented in a 100% vectorial PDF, generated using LaTeX and Overleaf, with no external images, adhering to IEEE style.

## Project Structure

quantum-trading-thermal-stability/
├── LICENSE                           # Creative Commons Attribution 4.0 License
├── Quantum_Trading_Thermal_Stability.pdf  # Compiled vectorial PDF report
├── README.md                        # Project documentation
├── cmb_results.tex                  # CMB results table
├── counts.dat                      # Data for QRL counts histogram
├── main.tex                       # Main LaTeX source document
├── p_error.dat                    # Data for fidelity vs. ΔT plot
├── qrl_cmb_simulation.py          # Python simulation script
└── references.bib                 # Bibliography in IEEE style

## Requirements
'''
- **Overleaf Account**: For compiling the LaTeX document.
- **Python Environment** (to regenerate data files, optional):
  - Python 3.8+
  - Libraries: `astropy`, `qiskit`, `pandas`
  - Install: `pip install astropy qiskit pandas`
- **CMB Data**: Download `COM_CMB_IQU-smica-field-Int_2048_R3.00.fits` from [Planck Legacy Archive](https://pla.esac.esa.int/pla/#maps) if regenerating data files.
'''

## Setup and Compilation

1. **Create an Overleaf Project**:
   - Log in to [Overleaf](https://www.overleaf.com).
   - Create a new project and upload all files listed in the project structure (except the PDF).
   - Ensure all files are encoded in UTF-8 to avoid errors.
   - Alternatively, download the compiled PDF: [Quantum_Trading_Thermal_Stability.pdf](Quantum_Trading_Thermal_Stability.pdf).

2. **Generate Data Files** (optional, if you need to regenerate):
   - Run `qrl_cmb_simulation.py` locally to generate:
     - `cmb_results.tex`: CMB results table.
     - `p_error.dat`: Fidelity vs. ΔT data.
     - `counts.dat`: QRL counts data.
   - Requirements:
     - Place `COM_CMB_IQU-smica-field-Int_2048_R3.00.fits` in the same directory as the script.
     - Install dependencies: `pip install astropy qiskit pandas`.
     - Run: `python qrl_cmb_simulation.py`.
   - Expected output:
     - Cycle: 91 days
     - Rewards: ~34.1% +1, ~33.0% -1, ~33.0% 0
     - Fidelity: ~93.7%
     - Files: `cmb_results.tex`, `p_error.dat`, `counts.dat`

3. **Compile the PDF**:
   - In Overleaf, set the compiler to `pdfLaTeX`.
   - Ensure all files are in the root directory and encoded in UTF-8.
   - Compile `main.tex` to generate the PDF.
   - Verify:
     - CMB table shows ~93.7% fidelity.
     - PGFPlots graphs (histogram and fidelity vs. ΔT) render correctly.
     - Python code listing in the appendix is readable.
     - IEEE references appear in text (e.g., [1]) and bibliography.
     - PDF is 100% vectorial (check graphs in Adobe Acrobat at high zoom).

4. **Troubleshooting**:
   - **PGFPlots errors** (e.g., „Could not parse input '...'”):
     - Ensure `p_error.dat` has 91 lines, no invalid entries (e.g., „...”), and no empty lines.
     - Regenerate `p_error.dat` using `qrl_cmb_simulation.py` if needed.
     - Verify `main.tex` uses `unbounded coords=jump` and `restrict x to domain=0:0.1`.
   - **UTF-8 errors**:
     - Save all files (especially `qrl_cmb_simulation.py` and `p_error.dat`) in UTF-8 encoding.
     - In editors like VS Code, select „Save with Encoding” → UTF-8.
   - **Math mode errors**:
     - Ensure file names with underscores (e.g., FITS file in `main.tex`) use `\discretionary{-}{}{}` for hyphenation.
   - **Overfull \hbox warnings**:
     - The financial table uses `\scriptsize`, and paragraphs have hyphenation enabled to minimize warnings. Minor warnings may persist but do not affect the PDF.

5. **Access the PDF**:
   - Download the compiled PDF from Overleaf or use [Quantum_Trading_Thermal_Stability.pdf](Quantum_Trading_Thermal_Stability.pdf).
   - Confirm the PDF is vectorial by zooming in on graphs in Adobe Acrobat.

## Notes

- The project uses an adaptive noise model with \( p_{\text{error}} = 0.05 + 0.0003 \cdot |\Delta T| \), achieving a fidelity of ~93.7%.
- The PDF is 100% vectorial, using TikZ/PGFPlots for graphs and tables, with no external images.
- The project adheres to IEEE style for citations and formatting.
- Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
- Repository: [https://github.com/DonMask/quantum-trading-thermal-stability](https://github.com/DonMask/quantum-trading-thermal-stability)

## GitHub Setup

1. **Verify All Files**:
   - Ensure the repository contains all files listed in the project structure.
   - If any files are missing, upload them using Git or GitHub's web interface:
     ```bash
     git clone https://github.com/DonMask/quantum-trading-thermal-stability.git
     cd quantum-trading-thermal-stability
     # Copy files
     git add .
     git commit -m "Add all project files with fixed PGFPlots and UTF-8 issues"
     git push origin main
     ```

2. **Create a Release**:
   - Go to the „Releases” section on GitHub.
   - Create a new release:
     - Tag: `v1.0.0`
     - Title: „Initial Release: QRL with 93.7% Fidelity”
     - Attach `Quantum_Trading_Thermal_Stability.pdf` and a ZIP of all files.
     - Publish the release.

3. **Share on X**:
   - Post: „Finalized QRL with adaptive fidelity (p_error = 0.05 + 0.0003·|ΔT|), achieving ~93.7% fidelity for CMB and BTC. IEEE-style PDF, 100% vectorial with TikZ. Licensed under CC BY 4.0. Check it out: https://github.com/DonMask/quantum-trading-thermal-stability #QuantumTrading #Planck”

## License

This project is licensed under the Creative Commons Attribution 4.0 International License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or contributions, contact Teodor Berger at bergerteodor@googlemail.com.
