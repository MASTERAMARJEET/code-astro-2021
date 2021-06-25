# SpectroBinary

SpectroBinary is a Python package that is aimed to help in the study of Spectroscopic binary systems. The current version contains functions to simulate a binary system, and to find the Doppler shift from atomic spectroscopy data.

## Installation

```bash
pip install SpectroBinary
```

## Documentation

```bash


```

## SpectroBinary.doppler_shift()

This module analyses the spectral data at a given point in time, and calculates the Doppler shift. It looks for characteristic spectral lines in the data, and matches it with a template spectroscopy data which has no Doppler shift.

During the motion of the binary system about its center of mass, its radial velocity is towards the observer in some places in its orbit, and away from the observer at other places. This leads to a Doppler shift in the spectrum. The analysis of the spectrum over time can be used to characterize the parameters of the binary system, such as the mass ratios, orbital time period, etc.

## SpectroBinary.trajectory()

This module is used to simulate a binary system, with given masses. It assumes only the presence of gravitational force, and assumes a constant separation between the masses, leading to concentric circular orbits.
