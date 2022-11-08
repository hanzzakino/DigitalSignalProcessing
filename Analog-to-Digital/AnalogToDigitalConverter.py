'''
@author: Hanz Aquino
'''
__author__ = 'Hanz Aquino'
__version__ = '$Revision: 1.0 $'
__date__ = '$Date: 2022-09-23 $'

import math
from typing import Callable
import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import make_interp_spline

#Display the wave at a number of samples
#Process similar to integration
def quantize(wave_function:Callable, start:int, end:int, sampling_rate:int, amplitude_scale = 1):

    #The sum of each strip (Integral)
    #Strip = samplelength*f(t)
    total_area = 0

    #time difference of each sample
    step_size = 1/sampling_rate

    #Contained the list of area of each strip (Integral)
    sampleArea_list = []

    #Contained the list of amplitude of each sample
    amplitude_list = []

    #Contained the list of timestep of each sample (from t=0 to t=1, steps=1/samples)
    timestep_list = []

    #Loop at every sample
    for spl in range(0, int((end-start)/step_size)):

        #Current area value
        curretntStripArea = (step_size*wave_function(step_size*spl))

        #Store the curent strip area value
        sampleArea_list.append(curretntStripArea)

        #Store the curent sample value (y-value)
        amplitude_list.append(wave_function(step_size*spl)*amplitude_scale)

        #Store the time steps
        timestep_list.append((spl/sampling_rate)+start)

        #Add the area to the total area sum (Integral)
        total_area += curretntStripArea
    
    #Return data as dictionary (JSON)
    return {
            "total_area":total_area,
            "amplitude_list":amplitude_list,
            "timestep_list":timestep_list,
            }


def showSamplingComparisson(wave_function:Callable, start:int, end:int, *sampling_rate:int, amplitude_scale=1, interpolate=False, interpolation_sampling=48000):

    #List of matplotlib line colors
    colors = ['black','blue','red','green','magenta','yellow','cyan','white']

    #Iterate on each sampling rate argument
    for inx,spr in enumerate(sampling_rate):

        #Get sampling data
        quantized = quantize(wave_function, start, end, spr, amplitude_scale)

        if interpolate:
            #Convert result list to numpy array 
            x = np.array(quantized["timestep_list"])
            y = np.array(quantized["amplitude_list"])
            #Create a Spline function
            X_Y_Spline = make_interp_spline(x, y)
    
            # Returns evenly spaced numbers over a specified interval.
            X_ = np.linspace(x.min(), x.max(), interpolation_sampling)
            # Obtain all y values using upsampled x-array 
            Y_ = X_Y_Spline(X_)
            
            #Add subplot
            float_format = "{0:.2f}"
            plt.plot(
                X_,
                Y_,
                color = colors[inx%len(colors)],
                label=f'{spr} Hz - (L = {float_format.format(interpolation_sampling/spr)})'
            )
        else:
            #Add subplot
            plt.plot(
                quantized["timestep_list"],
                quantized["amplitude_list"],
                color = colors[inx%len(colors)],
                label=f'{spr} Hz'
            )

    #Plot details
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend(title='Sampling rate:')
    plt.title('Sampling Rate Comparisson (Interpolated)' if interpolate else 'Sampling Rate Comparisson')
    plt.show()

# def convertToBitSequence(wave_function, sampling_rate, bitdepth=24):
    



def a(x):
    return (0.3*math.sin(x))+(0.7*math.sin(4*x))+(0.2*math.sin(20*x))+(0.1*math.sin(50*x))+(0.7*math.sin(3*x))

def b(x):
    return (-(1/4)*math.sin(3*math.pi*x))+((3/4)*math.sin(math.pi*x))+(-(1/2)*math.sin(math.pi*x))+(((3**0.5)/2)*math.cos(math.pi*x))

showSamplingComparisson(a, 0, 5, 3, 6, 28, 56, 48000, amplitude_scale=10000, interpolate=True)
