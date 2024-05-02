from curvas import Perten
import numpy as np
from fuzzy import Fuzzy
import json
import matplotlib.pyplot as plt
import csv
import pandas as pd
#Cargar datos

days = []
with open('temps.json') as file:
    data = json.load(file)
    for i in data:
        days.append(np.array(i))

# days = [[10, 9, 9, 9, 10, 10, 11, 11, 27, 28, 28, 29, 29, 30, 31, 31, 30, 30, 30, 29, 29, 28, 28, 27],
#         [10, 9, 9, 9, 10, 10, 11, 11, 27, 28, 28, 29, 29, 30, 31, 31, 30, 30, 30, 29, 29, 28, 28, 27]]
# days = [np.array(i) for i in days]


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
tmin = Perten("c", True, 5, 25, [0, 35], 0, 0.8)
t= Perten("m", False, 22, 4, [0, 35], 0.5)
tmax = Perten("a", True, 25, 35, [0, 35], 0.2, 1)

tInt = 27
tInts = [27]
Apers = []
tDays = []

ctrol = Fuzzy([neg, zero, pos], [cl, mid, op], [ad, md, ng], [tmin, t, tmax])

for j in range(len(days)-1):

    for i in range(len(days[j])):

        tInt, pAper = ctrol.solution(days[j][i], tInt,i,days[j + 1].mean())


        tInts.append(tInt)
        Apers.append(pAper)

   #print('Temperatura del día:            '+ str(tDia))
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

# Add labels for the x and y axes
plt.xlabel('Tiempo (Hs)')
plt.ylabel('(u)')
# plt.plot(tInts, label='Temperatura Interna')
# plt.legend()
# #plt.show()
# plt.plot(unir, label='Temperatura externa', color='red')
# plt.legend()
# plt.plot(Apers, label='Apertura', color='orange')
# plt.legend()
# plt.show()

ad.plot()
md.plot()
ng.plot()
plt.show()


