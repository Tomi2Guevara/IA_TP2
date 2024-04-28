from curvas import Perten
from antecedente import Antecedent
import numpy as np
from fuzzy import Fuzzy

#curvas de pertenencia
#variables de entrada
neg = Perten("n", True, -25, 0,[-35, 35], 0, 0.6 )
zero = Perten("z", False, -5, 10, [-35, 35], 0.5)
pos = Perten("p", True, 0, 25, [-35, 35], 0.4, 1)
cl = Perten("c", True, 0, 50, [0, 100], 0, 0.6)
mid = Perten("m", False, 45, 10, [0, 100], 0.5)
op = Perten("a", True, 50, 100, [0, 100], 0.4, 1)

d1 = np.random.uniform(10, 30, 24)
d2 = np.random.uniform(10, 30, 24)
d3 = np.random.uniform(10, 30, 24)
d4 = np.random.uniform(10, 30, 24)
days = [d1, d2, d3, d4]
temp_p_Hora = {}

tInt = 27

ctrol = Fuzzy([neg, zero, pos], [cl, mid, op])

for j in range(len(days)-2):
    for i in range(len(days[j])):
        temp_p_Hora[str(i)] = days[j][i]
    for i in range(24):
        if 7 <= temp_p_Hora[str(i)] < 20:
            tInt = ctrol.solution(temp_p_Hora[str(i)], tInt, 25)
            #print(tInt)

        elif days[j+1].mean() > 25:
            tInt = ctrol.solution(temp_p_Hora[str(i)], tInt, 10)

        elif days[j+1].mean() < 25:
            tInt = ctrol.solution(temp_p_Hora[str(i)], tInt, 35)

print(tInt)


