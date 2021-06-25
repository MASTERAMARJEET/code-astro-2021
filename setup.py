from setuptools import setup, find_packages

LONG_DESC = "SpectroBinary is a Python package that is aimed to help in the study of Spectroscopic binary systems. The current version contains functions to simulate a binary system, and to find the Doppler shift from atomic spectroscopy data."

setup(
    name="SpectroBinary",
    version="1.0.0",
    author="Amarjeet Kumar, Bhuvanambiga Pari",
    author_email="masteramarjeetkumar@gmail.com",
    license="MIT",
    long_description=LONG_DESC,
    url="https://github.com/MASTERAMARJEET/code-astro-2021",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
)

