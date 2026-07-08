# Active Low-Pass Filter Design

This project designs an active Butterworth low-pass filter and validates the component choices in LTspice.

## Design Targets

| Spec | Value |
|---|---:|
| Filter type | Butterworth low-pass |
| Order | 11 |
| Passband attenuation | 1 dB |
| Stopband attenuation | 25 dB |
| Passband frequency | 14 kHz |
| Stopband frequency | 20 kHz |
| Gain | 8 V/V |
| Resistor tolerance | 1% |
| Capacitor tolerance | 5% |

## Files

| File | Purpose |
|---|---|
| `filter_calculations.ipynb` | Butterworth order, pole, Q, and component calculations |
| `LPF.asc` | LTspice low-pass filter schematic |
| `onepole.asy` | LTspice symbol used in the filter schematic |
| `OPAMP.sub` | Op-amp subcircuit model |
| `filter_design_report.pdf` | Final report |

## Design Notes

The design uses five second-order Sallen-Key stages plus a first-order gain stage. The calculation notebook derives the Butterworth pole locations, Q values, and component values for each stage. The LTspice schematic includes tolerance stepping for Monte Carlo-style robustness checks.

