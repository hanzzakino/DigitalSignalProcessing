import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import math
from numpy.typing import NDArray



def getFourierSeries(dataSamples:NDArray, timeDuration:int, maxFrequency:int, resFrequency:float, interpolationSampling =-1):
    
    print('=== Start ===')

    n = len(dataSamples)

    # Upscale the sampling rate of the dataSamples if needed
    # i.e. if the dataSamples has 1200 samples and the timeDuration is set to be 5s
    # the sampling rate would be 1200samples/5seconds or  240 samples/second
    samplingRate = math.floor(n/timeDuration)
    if interpolationSampling > 1:
        print('Interpolating...')
        y = np.array(dataSamples[:samplingRate*timeDuration])
        x = np.array([i for i in range(samplingRate*timeDuration)])
        #Create a Spline function
        X_Y_Spline = make_interp_spline(x, y)
        # Returns evenly spaced numbers over a specified interval.
        X_ = np.linspace(x.min(), x.max(), interpolationSampling)
        # Obtain all y values using upsampled x-array 
        dataSamples = X_Y_Spline(X_)
        n = len(dataSamples)
  

    print('Computing Fourier series...')
    
    frequencyDivisions = math.floor(maxFrequency/resFrequency)
 
    fourier = np.array([
        sum(math.sin(2*math.pi*(freq*resFrequency)*(x*(timeDuration/n)))*dataSamples[x] for x in range(n))
        for freq in range(frequencyDivisions)
    ])

    print('Showing...')

    figure, axis = plt.subplots(2)

    axis[0].plot(np.array([i*(timeDuration/n) for i in range(n)]),dataSamples)
    axis[0].set_title("Time Domain")

    axis[1].plot(np.array([i*resFrequency for i in range(len(fourier))]),fourier)
    axis[1].set_title("Frequency Domain")

    plt.show()

    print('=== Done ===')

def generateFourierSeriesFile(outputFile:str , dataSamples:NDArray, timeDuration:int, maxFrequency:int, resFrequency:float, interpolationSampling =-1):
    print('=== Start ===')
    n = len(dataSamples)
    # Upscale the sampling rate of the dataSamples if needed
    # i.e. if the dataSamples has 1200 samples and the timeDuration is set to be 5s
    # the sampling rate would be 1200samples/5seconds or  240 samples/second
    samplingRate = math.floor(n/timeDuration)
    if interpolationSampling > 1:
        print('Interpolating...')
        y = np.array(dataSamples[:samplingRate*timeDuration])
        x = np.array([i for i in range(samplingRate*timeDuration)])
        #Create a Spline function
        X_Y_Spline = make_interp_spline(x, y)
        # Returns evenly spaced numbers over a specified interval.
        X_ = np.linspace(x.min(), x.max(), interpolationSampling)
        # Obtain all y values using upsampled x-array 
        dataSamples = X_Y_Spline(X_)
        n = len(dataSamples)


    print('Writing Fourier series...')

    frequencyDivisions = math.floor(maxFrequency/resFrequency)

    file = open(f'Discrete-Fourier-Transform/output-files/{outputFile}','w')
    with file as ff:
        for freq in range(frequencyDivisions):
            if freq == frequencyDivisions-1:
                ff.write(str(sum(math.sin(2*math.pi*(freq*resFrequency)*(x*(timeDuration/n)))*dataSamples[x] for x in range(n))))
            else:
                ff.write(str(sum(math.sin(2*math.pi*(freq*resFrequency)*(x*(timeDuration/n)))*dataSamples[x] for x in range(n)))+'\n')

    print('=== Done ===')








# TEST
# w = lambda x : math.sin(2*math.pi*25*x) + math.sin(2*math.pi*7*x) + math.sin(2*math.pi*14*x)
# dataSet = np.array([w(x/2000) for x in range(12000)])

# file = open('2 khz','w')

# with file as ff:
#     for d in dataSet:
#         ff.write('\n'+str(d))


# file = open('2 khz','r')
# dataSet = np.array(file.readlines()).astype(float)

# getFourierSeries(
#     dataSamples = dataSet,
#     timeDuration=6,
#     maxFrequency=30,
#     resFrequency=0.1,
#     interpolationSampling=15000
# )

