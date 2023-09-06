import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.figure as fig
from numpy.random import default_rng
import time 
 
l = 0    
Dadosx= []
dadosy= []
rng = default_rng()
aleat = rng.integers(10,size = (4,2))

    
while True:
    l = l + 1
    rng = default_rng()
    aleat = rng.integers(10,size = (4,2))
    print(f'{aleat}')
    for c in range(len(aleat)):
        for i in range(len(aleat)):
            if i == 1:
                Dadosx.append(aleat[c][i])
            if i == 0:
                dadosy.append(aleat[c][i])
    print(f'{Dadosx}')
    print(f'{dadosy}')
    plt.plot(Dadosx,dadosy)
    plt.show()
    dadosy.clear()
    Dadosx.clear()
    if l == 1:
        break
np.save('Dadosaleator.npy', aleat)

a2 = np.load('Dadosaleator.npy')
print(f'{a2}')