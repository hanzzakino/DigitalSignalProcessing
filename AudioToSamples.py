import matplotlib.pyplot as plt
import math
from scipy.io.wavfile import read
from DFT import getFourierSeries

bnote = read('b.wav')
print(bnote[0])

samples = bnote[1][:22050]

# file = open('b-note','w')

# with file as f:
#     for s in samples:
#         f.write(str(s)+'\n')

getFourierSeries(dataSamples=samples,timeDuration=1,maxFrequency=10000, resFrequency=0.5)