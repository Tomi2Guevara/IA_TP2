from curvas import Perten
import numpy as np
from fuzzy import Fuzzy
import json
import matplotlib.pyplot as plt
import csv
import pandas as pd
#Cargar datos

# days = []
# with open('temps.json') as file:
#     data = json.load(file)
#     for i in data:
#         days.append(np.array(i))

days = [[10, 9, 9, 9, 10, 10, 11, 11, 27, 28, 28, 29, 29, 30, 31, 31, 30, 30, 30, 29, 29, 28, 28, 27],
        [10, 9, 9, 9, 10, 10, 11, 11, 27, 28, 28, 29, 29, 30, 31, 31, 30, 30, 30, 29, 29, 28, 28, 27]]
days = [np.array(i) for i in days]


#curvas de pertenencia
#variables de entrada
neg = Perten("n", True, -35, 0,[-35, 35], 0, 0.90)
zero = Perten("z", False, -1, 2, [-35, 35], 0.5)
pos = Perten("p", True, 0, 35, [-35, 35], 0.10, 1)
cl = Perten("c", True, 0, 50, [0, 100], 0, 0.8)
mid = Perten("m", False, 48, 4, [0, 100], 0.5)
op = Perten("a", True, 50, 100, [0, 100], 0.2, 1)


#d1 = np.random.uniform(10, 30, 24)
#d2 = np.random.uniform(10, 30, 24)
#d3 = np.random.uniform(10, 30, 24)
#d4 = np.random.uniform(10, 30, 24)
#temp_p_Hora = {}

tInt = 27
tInts = [27]
Apers = []
tDays = []

ctrol = Fuzzy([neg, zero, pos], [cl, mid, op])

for j in range(len(days)-1):

    for i in range(len(days[j])):
        #Subconjuntos:

        if 7 < i:
            if i < 20:
                tInt, pAper = ctrol.solution(days[j][i], tInt, 25)
                tDia = tInt
                tDays.append(tDia)
                #print(tInt)
            elif days[j + 1].mean() > 25:
                tInt, pAper = ctrol.solution(days[j][i], tInt, 5)

            elif days[j + 1].mean() < 20:
                tInt, pAper = ctrol.solution(days[j][i], tInt, 40)

        elif days[j].mean() > 25:
            tInt, pAper = ctrol.solution(days[j][i], tInt, 5)

        elif days[j].mean() < 25:
            tInt, pAper = ctrol.solution(days[j][i], tInt, 40)

        tInts.append(tInt)
        Apers.append(pAper)

    print('Temperatura del día:            '+ str(tDia))
    print('Temperatura promedio del día:   ' + str(days[j].mean()))
    print('' +
          '---------------------------------')

#unir los primero tres elementos de days en un vector
unir = []
count = 0
for i in days:
    count += 1
    if count == 2:
        break
    for j in i:
        unir.append(j)
#unir = np.concatenate(days[:3]).flatten()

#graficar en el mismo grapico Apers y tInts
# Add a title
plt.title('Temperatura y Apertura por tiempo')

# Add labels for the x and y axes
plt.xlabel('Tiempo (Hs)')
plt.ylabel('Temperatura (°C)')
plt.plot(tInts, label='Temperatura Interna')
plt.legend()
#plt.show()
plt.plot(unir, label='Temperatura externa', color='red')
plt.legend()
plt.plot(Apers, label='Apertura', color='orange')
plt.legend()
plt.show()


