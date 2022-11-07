import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import math

# colors = ['black','blue','red','green','magenta','yellow','cyan','white']

# samples = [0,0.2,0.67,0.34,0.12,0.67,0.97,0.12,0.45,0.50,0.78]
# length = len(samples)
# timeVal = [i for i in range(len(samples))]

# def getComplexSamples(sample_list,n):
#     return [
#             sum(sample_list[j] * math.e**((-2j*math.pi*j*k)/n) for j in range(n))
#             for k in range(n)
#         ]

# for z in getComplexSamples(samples,length):
#     #A = math.atan2(z.imag,z.real)
#     print(f"{z.real} + {z.imag}i","\n")

# # cplx = A + Bi
# # mag = sqrt(A^2 + B^2)
# # THETA = arctan(B/A)


# def showPlot(sample_list, time_list, interpolate = False):
#     if(interpolate):
#         #Convert result list to numpy array 
#         interpolation_sampling = 48000
#         x = np.array(sample_list)
#         y = np.array(time_list)
#         #Create a Spline function
#         X_Y_Spline = make_interp_spline(x, y)
#         # Returns evenly spaced numbers over a specified interval.
#         X_ = np.linspace(x.min(), x.max(), interpolation_sampling)
#         # Obtain all y values using upsampled x-array 
#         Y_ = X_Y_Spline(X_)
#         plt.plot(X_,Y_,color = colors[1],)
#     else:
#         plt.plot(time_list,sample_list,color = colors[0])
#     plt.show()

# n = 150
# max_frequency = 15*3000

# w = lambda x : (math.sin(2*math.pi*2*x) + math.sin(2*math.pi*6*x))



# frequencies = [[math.sin(2*math.pi*(f/3000)*(x/150)) for x in range(n)] for f in range(max_frequency)]

# #print(samples,'\n', frequencies[1])


# fourier = []
# for freq in frequencies:
#     fourier.append(sum(samples[i]*freq[i] for i in range(n)))


# plt.plot([i/3000 for i in range(max_frequency)], fourier)
# #plt.plot([i for i in range(n)], samples)
# plt.show()

def getFourierSeries(dataSamples:list, timeDuration:int, maxFrequency:int, resFrequency:float, interpolationSampling =-1):
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
    
    print('Creating sine waves matrix...')
    frequencyDivisions = math.floor(maxFrequency/resFrequency)
    sineWaves = [[math.sin(2*math.pi*(freq*resFrequency)*(x*(timeDuration/n))) for x in range(n)] for freq in range(frequencyDivisions)]

    # print(n)
    
    
    print('Computing Fourier series...')
    fourier = []
    flen = 0
    for sineWave in sineWaves:
        fourier.append(sum(dataSamples[i]*sineWave[i] for i in range(n)))
        flen += 1



    print('Showing...')

    figure, axis = plt.subplots(2)

    axis[0].plot([i*(timeDuration/n) for i in range(n)],dataSamples)
    axis[0].set_title("Time Domain")

    axis[1].plot([i*resFrequency for i in range(flen)],fourier)
    axis[1].set_title("Frequency Domain")

    plt.show()


    print('=== Done ===')


w = lambda x : math.sin(2*math.pi*25*x) + math.sin(2*math.pi*7*x) + math.sin(2*math.pi*14*x)
dataSet = [w(x/100) for x in range(400)]



getFourierSeries(dataSamples=dataSet,timeDuration=4,maxFrequency=30,resFrequency=0.01,interpolationSampling=5000)

