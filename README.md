# Quantum Trading with Thermal Stability

This project implements a Quantum Reinforcement Learning (QRL) model integrating financial (Bitcoin) and cosmological (CMB) data, achieving high fidelity (~93.7%) under simulated thermal noise. The project is documented in a 100% vectorial PDF, generated using LaTeX and Overleaf, with no external images, adhering to IEEE style.

## Project Structure
```
quantum-trading-thermal-stability/
├── LICENSE                                - Creative Commons Attribution 4.0 License
├── Quantum_Trading_Thermal_Stability.pdf  - Compiled vectorial PDF report
├── README.md                              - Project documentation
├── cmb_results.tex                        - CMB results table
├── counts.dat                             - Data for QRL counts histogram
├── main.tex                               - Main LaTeX source document
├── p_error.dat                            - Data for fidelity vs. ΔT plot
├── qrl_cmb_simulation.py                  - Python simulation script
└── references.bib                         - Bibliography in IEEE style
```
## Requirements

- **Overleaf Account**: For compiling the LaTeX document.
- **Python Environment** (to regenerate data files, optional):
  - Python 3.8+
  - Libraries: `astropy`, `qiskit`, `pandas`
  - Install: `pip install astropy qiskit pandas`
- **CMB Data**: Download `COM_CMB_IQU-smica-field-Int_2048_R3.00.fits` from [Planck Legacy Archive](https://pla.esac.esa.int/pla/#maps) if regenerating data files.
'''

## Setup

1. **Compile in Overleaf**:
   - Log in to [Overleaf](https://www.overleaf.com).
   - Upload all files (except PDF) to a new project.
   - Set compiler to `pdfLaTeX` and compile `main.tex`.
   - Check:
     - CMB table: ~93.7% fidelity.
     - Graphs: Histogram and fidelity vs. ΔT.
     - PDF: Vectorial (clear at zoom in Adobe Acrobat).
   - Download PDF as `Quantum_Trading_Thermal_Stability.pdf`.

2. **Regenerate Data (Optional)**:
   - Run `qrl_cmb_simulation.py` locally:
     - Download `COM_CMB_IQU-smica-field-Int_2048_R3.00.fits` from [Planck Legacy Archive](https://pla.esac.esa.int/pla/#maps).
     - Install: `pip install astropy qiskit pandas`.
     - Run: `python qrl_cmb_simulation.py`.
     - Outputs: `cmb_results.tex`, `p_error.dat`, `counts.dat`.

3. **Troubleshooting**:
   - **PGFPlots errors**: Ensure `p_error.dat` has 91 lines, no „...”. Regenerate if needed.
   - **UTF-8 errors**: Save files in UTF-8 (VS Code: „Save with Encoding” → UTF-8).
   - **Math mode errors**: FITS file name in `main.tex` uses `\discretionary{-}{}{}`.

## Access
- GitHub: [https://github.com/DonMask/quantum-trading-thermal-stability](https://github.com/DonMask/quantum-trading-thermal-stability)
- Zenodo: https://doi.org/10.5281/zenodo.15420886

## Citation
```bibtex
@misc{berger_2025_quantum_trading,
  author       = {Teodor Berger},
  title        = {Quantum Trading with Thermal Stability: QRL Model for Bitcoin and CMB Data},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15420886},
  url          = {https://doi.org/10.5281/zenodo.15420886}
}
```
## License

This project is licensed under the Creative Commons Attribution 4.0 International License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or contributions, contact Teodor Berger at bergerteodor@googlemail.com.
