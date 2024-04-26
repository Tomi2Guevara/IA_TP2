from scipy.stats import trapz, triang
import numpy as np
import matplotlib.pyplot as plt


class Antecedente():
    def __init__(self, name, trap, sta, end, ch1 = 0.5 , ch2 = None, dom = []):
        self.type = trap
        self.name = name #variable linguistica
        self.range = dom

        # límites de la distribución (para trapezoidal es el inicio y fin de la figura)
        self.a = sta #inicio de la figura
        self.b = end #para triangulo es el ancho de la base

        # puntos de cambio(en porcentaje)
        self.c = ch1
        self.d = ch2

        #Dominio de la función
        self.x = np.linspace(0, dom, 1000)

    def select(self):
        if self.type:
            self.curva = trapz(self.c, self.d, loc=self.a, scale=self.b-self.a)
        else:
            self.curva = triang(self.c, loc=self.a, scale=self.b)

    def plot(self):
        plt.plot(self.x, self.curva.pdf(self.x) / self.curva.pdf(self.x).max(), label=self.name)
        plt.legend()
        plt.show()

    def eval(self, x):
        if x > self.rango[0] or x < self.rango[1]:
            return self.curva.pdf(x) / self.curva.pdf(self.x).max()
        else:
            return None
