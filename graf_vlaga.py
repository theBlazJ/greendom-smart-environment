# vstavljanje potrebnega modula
import matplotlib.pyplot as plt

# x os vrednosti
x = [0, 5, 10, 15, 20, 25]
# y os vrednosti
y = [28.11, 30.01, 23.31, 22.01, 22.11, 22.51 ]

# plotting the points
plt.plot(x, y)

# dodajanje imena x osi
plt.xlabel('Čas (od začetka delovanja v min)')

# dodajanje imena y osi
plt.ylabel('Vlaga (%)')

# dodajanje imena grafa
plt.title('Vlaga')

# funkcija za prikaz grafa
plt.show()


