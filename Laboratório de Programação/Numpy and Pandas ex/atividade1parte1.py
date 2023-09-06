import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.figure as fig
import random
import math

def defcentroids(k,Dadosx,dadosy,centroids):#define o número e posição aleatória dos centróides
    l = 0
    while True:
        l = l + 1 
        if l != (k+1):
            centroids.append([random.choice(Dadosx),random.choice(dadosy)])
        else:
            break
    return  
  
def euclidian(k,centroids,Dadosx,dadosy):#o que vai ser plotado sai da última iteração com os centróides
    for i in range(len(Dadosx)):
    #os clusters precisam ser criados com base na primeira interação e dependem dos centróides para ser preenchidos
    
def separadados(aleat):
    for c in range(len(aleat)):
        for i in range(len(aleat)):
            if i == 1:#tá criado errado aqui, pois pega por linha e não por coluna devia ser
                Dadosx.append(aleat[c][i])
            if i == 0:
                dadosy.append(aleat[c][i])       
Dadosx= []
dadosy= []
centroids=[]
k = int(input('Digite o número de centróides:'))
a2 = np.load('Dadosaleator.npy')
print(f'{a2}')
separadados(a2)
defcentroids(k,Dadosx,dadosy,centroids)
euclidian(centroids,Dadosx,dadosy)

print(f'{centroids}')
print(f'{Dadosx}')
print(f'{dadosy}')       
plt.plot(Dadosx,dadosy)
plt.show()