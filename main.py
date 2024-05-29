from curvas import Perten
import numpy as np
from fuzzy import Fuzzy
import json
import matplotlib.pyplot as plt
import csv
import pandas as pd
#Cargar datos

#Crae datos a partir de una onda senoidal
t = np.linspace(0, 24, 24)
t = np.sin(0.5*t)
t1 = t * 5 + 25
t2 = t * 10 + 30
t3 = t * 15 + 20
# t = t + np.random.normal(0, 1, 100)
days = [t1, t2, t3]

# days = [[30, 31, 31, 31, 30, 30, 29, 29, 16, 15, 15, 14, 13, 13, 12, 11, 11, 10, 10, 8, 7, 8, 10, 10],
#         [30, 31, 31, 31, 30, 30, 29, 29, 16, 15, 15, 14, 13, 13, 12, 11, 11, 10, 10, 8, 7, 8, 10, 10]]
days = np.array(days)
#curvas de pertenencia

neg = Perten("n", True, -35, 0,[-35, 35], 0, 0.90)
zero = Perten("z", False, -1, 2, [-35, 35], 0.5)
pos = Perten("p", True, 0, 35, [-35, 35], 0.10, 1)
#------------------
cl = Perten("c", True, 0, 50, [0, 100], 0, 0.8)
mid = Perten("m", False, 48, 4, [0, 100], 0.5)
op = Perten("a", True, 50, 100, [0, 100], 0.2, 1)
#------------------
ad = Perten("ad", True, 0, 9, [0, 24], 0, 0.78)
md = Perten("md", True, 7, 21, [0, 24], 0.1, 0.9)
ng = Perten("ng", True, 19, 24, [0, 24], 0.22, 1)
#------------------
tmin = Perten("Fría", True, 5, 28, [5, 40], 0, 0.65)
tmax = Perten("Caliente", True, 22, 40, [5, 40], 0.35, 1)

tInt = 27
tInts = [27]
Apers = []
tDays = []

ctrol = Fuzzy([neg, zero, pos], [cl, mid, op], [ad, md, ng], [tmin, tmax])

for j in range(len(days)-1):

    for i in range(len(days[j])):

        tInt, pAper = ctrol.solution(days[j][i], tInt,i,days[j + 1].mean())


        tInts.append(tInt)
        Apers.append(pAper*10)

    # print('Temperatura del día:            '+ str(tDia))
    print('Temperatura promedio del día:   ' + str(days[j].mean()))
    print('' +
          '---------------------------------')

#unir los primero tres elementos de days en un vector
unir = []
count = 0
for i in days:
    count += 1
    if count == 3:
        break
    for j in i:
        unir.append(j)
#unir = np.concatenate(days[:3]).flatten()

#graficar en el mismo grapico Apers y tInts
# Add a title
plt.title('Fusificador')

# # Add labels for the x and y axes
# plt.xlabel('Hora')
# plt.ylabel('Temperatura')
# plt.plot(tInts, label='Temperatura Interna')
# # plt.legend()
#
# plt.plot(unir, label='Temperatura externa', color='red')
# plt.legend()
# plt.show()
# plt.plot(Apers, label='Apertura', color='orange')
# plt.legend()
# plt.show()
