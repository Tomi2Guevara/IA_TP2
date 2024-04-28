from scipy.stats import trapz, triang
import numpy as np
import matplotlib.pyplot as plt


class Perten():

    def __init__(self, name, trap, sta, end, dom, ch1 = 0.5, ch2 = None):

        self.name = name  # variable linguistica
        self.rango = dom

        # límites de la distribución (para trapezoidal es el inicio y fin de la figura)
        #self.a = sta  # inicio de la figura
        #self.b = end  # para triangulo es el ancho de la base

        # puntos de cambio(en porcentaje)
        #self.c = ch1
        #self.d = ch2

        # Dominio de la función
        self.x = np.linspace(dom[0], dom[1], 1000)
        if trap:
            self.curva = trapz(ch1, ch2, loc=sta, scale=end - sta)
        else:
            self.curva = triang(ch1, loc=sta, scale=end)


    def plot(self):
            plt.plot(self.x, self.curva.pdf(self.x) / self.curva.pdf(self.x).max(), label=self.name)
            plt.legend()
            #plt.show()

    def eval(self, x):
        if x > self.rango[0] or x < self.rango[1]:
            return self.curva.pdf(x) / self.curva.pdf(self.x).max()
        else:
            return None

    def bisect_defuzzify(self, y):
        try:
            # Find the indices where the PDF values are greater than or equal to y
            indices = np.where(self.curva.pdf(self.x) / self.curva.pdf(self.x).max() >= y)

            # Get the x values corresponding to these indices
            x_values = self.x[indices]

            # The defuzzified value is the midpoint of these x values
            midpoint = (x_values.min() + x_values.max()) / 2
        except ValueError:
            if self.curva.pdf(y) / self.curva.pdf(self.x).max() >= 1:
                midpoint = y
            else:
                midpoint = 50
        finally:
            return midpoint