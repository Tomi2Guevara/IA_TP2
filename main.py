from curvas import Perten
from antecedente import Antecedent
import matplotlib.pyplot as plt

#curvas de pertenencia
#variables de entrada
neg = Perten("n", True, -25, 0,[-25, 25], 0, 0.6 )
zero = Perten("z", False, -5, 10, [-25, 25], 0.5)
pos = Perten("p", True, 0, 25, [-25, 25], 0.4, 1)
cl = Perten("c", True, 0, 50, [0, 100], 0, 0.6)
mid = Perten("m", False, 45, 10, [0, 100], 0.5)
op = Perten("a", True, 50, 100, [0, 100], 0.4, 1)


#variables de entrada
tExt = 25
tInt = 25
tObj  = 25

ez1 = tInt - tObj
dz1 = tExt - tInt

#Abtecedentes
ant = [neg, zero, pos]
ve = []
vd = []
for a in ant:
    ve.append(a.eval(ez1))
    vd.append(a.eval(dz1))

ez = Antecedent("eZ", ve)
dz = Antecedent("dZ", vd)

#Reglas
#mismo consecuente:
c = max(min(ez.val[0],dz.val[0]),min(ez.val[0],dz.val[1]),min(ez.val[1],dz.val[0]),min(ez.val[1],dz.val[2]), min(ez.val[2],dz.val[1]), min(ez.val[2],dz.val[2]))
a = max(min(ez.val[0],dz.val[2]),min(ez.val[2],dz.val[0]))
m = min(ez.val[1],dz.val[1])
#consc = [c,m,a]
#Conjunto borroso de salida
sc = cl.bisect_defuzzify(c)
sm = mid.bisect_defuzzify(m)
sa = op.bisect_defuzzify(a)

aper = (c*sc+ m*sm + a*sa)/(c+m+a)
print(aper)


