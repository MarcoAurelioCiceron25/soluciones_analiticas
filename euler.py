import numpy as np
import matplotlib.pyplot as plt

# Definición de la función diferencial
def f(t, y):
    return y

# Parámetros
h = 0.2
t0, tf = 0, 1
N = int((tf - t0) / h)
y0 = 1

# Método de Euler
t_values = [t0]
y_values = [y0]

t = t0
y = y0
for i in range(N):
    y = y + h * f(t, y)
    t = t + h
    t_values.append(t)
    y_values.append(y)

# Solución exacta
t_exact = np.linspace(t0, tf, 100)
y_exact = np.exp(t_exact)

# Gráfica
plt.plot(t_values, y_values, 'o-', label='Euler (h=0.2)')
plt.plot(t_exact, y_exact, '-', label='Solución exacta $e^t$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Método de Euler vs Solución Exacta')
plt.grid(True)
plt.show()
