import matplotlib.pyplot as plt
import numpy as np

def showOutputPlot(filename:str):
    file = open(filename,'r')
    d = np.array(file.readlines())
    f = np.array([i for i in range(len(d))])
    plt.plot(f,d)
    plt.show()
    


showOutputPlot('Discrete-Fourier-Transform/output-files/audio-fourier-cloud')
