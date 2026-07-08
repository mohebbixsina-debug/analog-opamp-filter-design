# Analog Op-Amp and Filter Design

This repository contains two analog electronics design projects: a two-stage CMOS operational amplifier and an active low-pass filter. The work combines hand calculations, LTspice simulation files, and final design reports.

The goal is to show the complete analog design workflow: starting from specifications, deriving component or transistor values, validating the circuit in simulation, and documenting the final performance.

## Projects

| Project | What it Contains |
|---|---|
| `op-amp-design/` | Two-stage CMOS op-amp sizing, LTspice test benches, and design report |
| `filter-design/` | 11th-order Butterworth low-pass filter calculations, LTspice schematic, and design report |

## Highlights

- Designed a CMOS two-stage op-amp from target gain, GBW, slew rate, noise, ICMR, and output swing specs.
- Sized MOS transistors analytically and validated the design with LTspice test benches.
- Designed an 11th-order Butterworth low-pass filter for a 14 kHz passband and 20 kHz stopband target.
- Split the filter into second-order Sallen-Key sections plus a first-order gain stage.
- Included calculation notebooks, LTspice schematics, symbols, model files, and final PDF reports.

## Repository Layout

```text
op-amp-design/
  op_amp_calculations.ipynb
  *.asc / *.asy LTspice files
  op_amp_design_report.pdf

filter-design/
  filter_calculations.ipynb
  LPF.asc
  OPAMP.sub
  filter_design_report.pdf

tests/
  validate_project.py
```

## Quick Check

Run the lightweight repository validation:

```bash
python tests/validate_project.py
```

This checks that the notebooks are valid JSON and that the expected design files are present.

## Notes

These projects are educational analog design work. The schematics and calculations are useful for reviewing design choices, simulation setup, and tradeoffs, but they should be revalidated before any real hardware implementation.

## CV Summary

Designed and simulated CMOS op-amp and active filter circuits using analytical sizing, frequency-response calculations, and LTspice validation.

