import numpy as np
import matplotlib.pyplot as plt

def spectrum_template(res,tol=5.0):
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
    intensity_template=np.zeros(len(wavelength_template))*0.001

    n_tol=int(0.5*tol/res)

    for i in range(len(wavelength_template)):
        if(abs(wavelength_template[i]-spectral_line[count])<=res):
            intensity_template[i-n_tol:i+n_tol]=1
            count+=1
            if(count==8):
                break
    
    return(intensity_template)

def spectrum_match(template,data_obs):
    """
    Moves the template as a window across the observed spectral data, and finds the inner product at each window.

    Args:
        template (numpy,float): Template function with impulses at characteristic wavelengths
        data_obs (numpy,float): Observed intensity data

    Returns:
        match (numpy,float): Inner product for each window
    """
    n_temp,n_obs=len(template),len(data_obs)
    data=np.zeros(n_obs+2*n_temp)
    data[n_temp-1:-(n_temp+1)] = data_obs
    
    match=np.zeros(n_obs+n_temp)

    for i in range(n_obs+n_temp):
        match[i]=np.sum(template*data[i:i+n_temp])    

    return match


def spectrum_doppler_shift(data,tol,spec_type='absorb'):
    """
    This function finds the doppler shift in spectral data.

    Args:
        data (2D numpy,float): 
            Observed spectral intensity data (no of rows = no of data points, no of cols = 2) 
            First column contains the wavelength, 2nd column contains corresponding intensity

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

    data_wavelength,data_intensity=data[:,0],data[:,1]
    res=data_wavelength[1]-data_wavelength[0]
    template = spectrum_template(res,tol)
    
    plt.plot(template)
    plt.plot(data_intensity)
    plt.savefig("1.png")
    
    max_match=0

    if (spec_type=='emit'):
        match = spectrum_match(template,data_intensity)
        max_match=np.where(match==max(match))
    else:
        match = spectrum_match(-template,data_intensity)
        max_match=np.where(match==min(match))

    #pick the correct index
    wavelength_obs = data_wavelength[0] + max_match[0]*res 
    high_template=7000 #corresponds to highest wavelength of the template
    dopp_shift = wavelength_obs - high_template

    return dopp_shift


