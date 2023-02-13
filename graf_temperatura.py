# vstavljanje potrebnega modula
import matplotlib.pyplot as plt

# x os vrednosti
x = [0, 5, 10, 15, 20, 25]
# y os vrednosti
y = [28.11, 28.33, 37.77, 40.01, 39.41, 38.41]

# plotting the points
plt.plot(x, y)

# dodajanje imena x osi
plt.xlabel('Čas od začetka delovanja v min')

# dodajanje imena y osi
plt.ylabel('Temperatura (°C)')

# dodajanje imena grafa
plt.title('Temperatura')

# funkcija za prikaz grafa
plt.show()
