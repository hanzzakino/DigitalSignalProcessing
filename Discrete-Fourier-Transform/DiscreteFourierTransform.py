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

    figure, main = plt.subplots(2)

    main[0].plot(np.array([i*(timeDuration/n) for i in range(n)]),dataSamples)
    main[0].set_title("Time Domain")

    main[1].plot(np.array([i*resFrequency for i in range(len(fourier))]),fourier)
    main[1].set_title("Frequency Domain")

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


def getDiscreteFourierTransform(dataSamples:NDArray, timeDuration:int, maxFrequency:int, resFrequency:float, interpolationSampling =-1):
    
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
        (
            sum( (math.e**(-2j*math.pi*(freq*resFrequency)*(x*(timeDuration/n)))).real * dataSamples[x] for x in range(n)),
            sum(-(math.e**(-2j*math.pi*(freq*resFrequency)*(x*(timeDuration/n)))).imag * dataSamples[x] for x in range(n))
        )
        for freq in range(frequencyDivisions)
    ])

    print('Showing...')

    plot1 = plt.subplot2grid((2,2),(0,0),colspan=2)
    plot2 = plt.subplot2grid((2,2),(1,0))
    plot3 = plt.subplot2grid((2,2),(1,1)) 

    plot1.plot(np.array([i*(timeDuration/n) for i in range(n)]),dataSamples)
    plot1.set_title("Time Domain")


    plot2.plot(np.array([i*resFrequency for i in range(len(fourier))]),[i[1] for i in fourier])
    plot2.set_title("Frequency Domain - Sine waves")


    plot3.plot(np.array([i*resFrequency for i in range(len(fourier))]),[i[1]+i[0] for i in fourier])
    plot3.set_title("Frequency Domain")

    plt.tight_layout()
    plt.show()

    print('=== Done ===')







# TEST
w = lambda x : math.sin(2*math.pi*25*x) + math.sin(2*math.pi*7*x) + math.sin(2*math.pi*14*x)
w2 = lambda x : math.sin(2*math.pi*2*x) + math.cos(2*math.pi*7*x) + math.sin(2*math.pi*13*x) + math.cos(2*math.pi*18*x)
dataSet = np.array([w2(x/1000) for x in range(8000)])

# file = open('2 khz','w')

# with file as ff:
#     for d in dataSet:
#         ff.write('\n'+str(d))


# file = open('Discrete-Fourier-Transform/input-files/2 khz','r')
# dataSet = np.array(file.readlines()).astype(float)

getDiscreteFourierTransform(
    dataSamples = dataSet,
    timeDuration=8,
    maxFrequency=24,
    resFrequency=0.1,
    interpolationSampling=5000
)

