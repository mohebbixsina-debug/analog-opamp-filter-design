# Two-Stage CMOS Op-Amp Design

This project designs a two-stage CMOS operational amplifier and validates it through LTspice test benches.

## Design Targets

| Spec | Target |
|---|---:|
| Supply | +/-2.5 V |
| Slew rate | about 5 V/us |
| Load capacitance | 5 pF |
| Input common-mode range | -1.3 V to 2.1 V |
| Output swing | about +/-2.2 V |
| Gain-bandwidth | about 5 MHz |
| Phase margin | 60 deg |
| DC gain | 80 dB |
| Input-referred noise target | 30 nV/sqrt(Hz) |

## Files

| File | Purpose |
|---|---|
| `op_amp_calculations.ipynb` | Analytical sizing calculations |
| `2OPAMP.asc` | Main LTspice op-amp schematic |
| `2OPAMP.asy` | LTspice symbol for reuse in test benches |
| `AC.asc` | AC response / gain-bandwidth test bench |
| `ICMR.asc` | Input common-mode range test bench |
| `NOISE.asc` | Noise simulation test bench |
| `OUTPUT SWING.asc` | Output swing test bench |
| `SLEW RATE.asc` | Slew-rate transient test bench |
| `op_amp_design_report.pdf` | Final report |

## Design Notes

The notebook computes bias currents, overdrive voltages, compensation capacitance, resistor biasing, and W/L ratios. The LTspice files then test the amplifier from several angles: AC response, slew behavior, output swing, ICMR, and noise.

