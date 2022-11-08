import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read
from DiscreteFourierTransform import generateFourierSeriesFile


def generateSamplesFromAudio(inputFile, outputFile:str, trimSeconds=1):
    audioFile = read(inputFile)
    samplingRate = audioFile[0]
    samples = np.array(audioFile[1][:int(samplingRate*trimSeconds)])
    n = len(samples)

    output = open('Discrete-Fourier-Transform/output-files/'+outputFile,'w')
    with output as f:
        for i in range(n):
            if i == n-1:
                f.write(str(samples[i]))
            else:
                f.write(str(samples[i])+'\n')

def generateDFTFromAudio(inputFile, outputFile:str, trimSeconds=1, maxFreq=1000, resFreq=1.0):
    audioFile = read(inputFile)
    samplingRate = audioFile[0]
    samples = np.array(audioFile[1][:int(samplingRate*trimSeconds)])
    generateFourierSeriesFile(outputFile=outputFile,dataSamples=samples,timeDuration=trimSeconds,maxFrequency=maxFreq,resFrequency=resFreq)




audioFilename = ('Discrete-Fourier-Transform/input-files/'+'b.wav')
generateDFTFromAudio(audioFilename,'audio-fourier',1,8000,0.1)