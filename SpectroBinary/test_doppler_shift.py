import numpy as np
import matplotlib.pyplot as plt
from doppler_shift import spectrum_doppler_shift

#end to end test
def test_doppler_shift():
    import numpy as np
    import matplotlib.pyplot as plt

    line_H_alpha,line_H_beta,line_H_gamma,line_H_delta=6562.8,4861.3,4340.5,4101.7
    line_G_band=4250
    line_Na=5800
    line_He_neutral,line_He_ion=4200,4400

    spectral_line=np.array([line_H_alpha,line_H_beta,line_G_band,line_H_delta,line_H_gamma,line_He_ion,line_He_neutral,line_Na])
    spectral_line=np.sort(spectral_line)
    true_doppler_shift=500
    spectral_line+=true_doppler_shift


    res,tol=0.1,10.0
    wavelength=np.arange(2000,7000,res) 
    intensity=0.03*np.random.normal(0,10,len(wavelength))
    count=0
    n_tol=int(0.5*tol/res)
    for i in range(len(wavelength)):
            if(abs(wavelength[i]-spectral_line[count])<=res):
                intensity[i-n_tol:i+n_tol]+=2
                count+=1
                if(count==8):
                    break

    intensity+=10

    data=np.zeros((len(wavelength),2))
    data[:,0],data[:,1]=wavelength,intensity

    dopp_shift=spectrum_doppler_shift(data,tol,'emit')
    print(dopp_shift)


test_spectrum_doppler_shift()
