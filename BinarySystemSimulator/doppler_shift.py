import numpy as np
import matplotlib.pyplot as plt

def spectrum_template(res,tol):
    """
    Creates a template to be matched with the spectroscopic data.
    Wavelength of the template window is 4000 to 7000 nm

    Args:
        res (int): Minimum resolvable wavelength
        tol (float): Tolerance

    Returns:
        A template spectrum with 1's where the characteristic lines are to be present, and 0 elsewhere
    """
    line_H_alpha,line_H_beta,line_H_gamma,line_H_delta=6562.8,4861.3,4340.5,4101.7
    line_G_band=4250
    line_Na=5800
    line_He_neutral,line_He_ion=4200,4400

    spectral_line=np.array([line_H_alpha,line_H_beta,line_G_band,line_H_delta,line_H_gamma,line_He_ion,line_He_neutral,line_Na])
    spectral_line=np.sort(spectral_line)
    count=0
    wavelength_template=np.arange(4000,7000,res)
    intensity_template=np.zeros(len(wavelength_template))

    n_tol=int(0.5*tol/res)

    for i in range(len(wavelength_template)):
        if(abs(wavelength_template[i]-spectral_line[count])<=res):
            intensity_template[i-n_tol:i+n_tol]=1
            count+=1
            if(count==8):
                break
    
    return(intensity_template)

def spectrum_match(template,data):
    """
    Moves the template as a window across the observed spectral data, and finds the inner product at each window.

    Args:
        template (numpy,float): Template function with impulses at characteristic wavelengths
        data (numpy,float): Observed intensity data

    Returns:
        match (numpy,float): Inner product for each window
    """


def spectrum_doppler_shift(data,spec_type='absorb'):
    """
    This function finds the doppler shift in spectral data.

    Args:
        data (numpy,float): Observed spectral intensity data
        spec_type (string):
            Input can either be 'emit' or 'absorb'
            'emit': corresponds to emission spectrum (look for the highest inner product)
            'absorb': corresponds to absorption spectrum (look for the lowest inner product)

    Returns:
        dopp_shift (float): redshift/blueshifted wavelength (in angstrom)

    Methods:
        spectrum_template(res,tol): Function to create a template spectrum with given resolution and tolerance
        spectrum_match(template,data): Function to find the inner product of template with observed data
    """


res,tol=0.1,10
wavelength=np.arange(4000,7000,res)
intensity=spectral_template(res,tol)
plt.plot(wavelength, intensity)
plt.savefig("spectrum template.png")

            
    