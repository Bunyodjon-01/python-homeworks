import numpy as np
import matplotlib.pyplot as plt

## task 1
x = np.linspace(-10, 10, 1000)
y = x ** 2 - 4 * x + 4
plt.plot(x, y, color = "blue", label = "f(x)")

plt.title("f(x) = x^2 - 4x + 4")
plt.xlabel("X array")
plt.ylabel("Y arrray")

plt.grid(True)
plt.legend()
plt.show()

## task 2
a = np.linspace(0, 2 * np.pi, 100)
sinx = np.sin(a)
cosx = np.cos(a)
plt.plot(a, sinx, color = "green", linestyle = "dashed", marker = "^", markevery = 10, markersize = 8, markerfacecolor = "purple", markeredgecolor = "yellow", label = "sinx")
plt.plot(a, cosx, color = "blue", linestyle = "dotted", marker = "*", markevery = 10, markersize = 15, markerfacecolor = "yellow", markeredgecolor = "red", label = "cosx")

plt.title("sinx, cosx")
plt.xlabel("X array")
plt.ylabel("Y array")
plt.legend()
plt.show()

## task 3
x = np.linspace(0, 10, 100)
x3 = x ** 3
sinx = np.sin(x)
ex = np.exp(x)
logx = np.log(x+1)

plt.subplot(2, 2, 1)
plt.plot(x, x3, color = "blue")
plt.title("x^3")

plt.subplot(2, 2, 2)
plt.plot(x, sinx, color = "green")
plt.title("sinx")

plt.subplot(2, 2, 3)
plt.plot(x, ex, color = "yellow")
plt.title("e^x")

plt.subplot(2, 2, 4)
plt.plot(x, logx, color = "red")
plt.title("log(x+1)")
plt.tight_layout(pad= 1.0)
plt.show()

## task 4

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.uniform(0, 100, 100)

plt.scatter(x, y, c = colors, marker = "o", cmap= "viridis", edgecolors="black")

plt.title("scatter plot")
plt.xlabel("X arrey")
plt.ylabel("Y arrey")
plt.grid(True)

plt.show()

## task 5

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(9, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

plt.title("Normal Taqsimot Gistogrammasi (1000 ta nuqta)", fontsize=14)
plt.xlabel("Qiymatlar oralig'i", fontsize=12)
plt.ylabel("Takrorlanish soni (Frequency)", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

## task 6
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 1. Ma'lumot tayyorlash
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

# 2. Grafik yaratish
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 3. Sirtni chizish
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# 4. Bezatish
ax.set_title("3D Surface Plot: f(x, y) = cos(x^2 + y^2)")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

# Ranglar panelini (colorbar) qo'shish
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.show()

## task 7
import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'orchid']

plt.figure(figsize=(10, 6))
plt.bar(products, sales, color=colors, edgecolor='navy')

plt.title("Mahsulotlar bo'yicha sotuv ko'rsatkichlari", fontsize=14)
plt.xlabel("Mahsulot nomi", fontsize=12)
plt.ylabel("Sotuv miqdori (dona)", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()

## task 8
import matplotlib.pyplot as plt
import numpy as np

periods = ['T1', 'T2', 'T3', 'T4']
cat_a = [15, 20, 25, 18]
cat_b = [10, 25, 15, 20]
cat_c = [5, 15, 20, 10]

plt.figure(figsize=(10, 6))

# Birinchi qatlam
plt.bar(periods, cat_a, label='Category A', color='#1f77b4')

# Ikkinchi qatlam (A ning ustiga qo'yiladi)
plt.bar(periods, cat_b, bottom=cat_a, label='Category B', color='#ff7f0e')

# Uchinchi qatlam (A va B ning yig'indisi ustiga qo'yiladi)
cat_a_b = np.add(cat_a, cat_b)
plt.bar(periods, cat_c, bottom=cat_a_b, label='Category C', color='#2ca02c')

plt.title("Vaqt davrlari bo'yicha toifalar hissasi (Stacked Bar Chart)", fontsize=14)
plt.xlabel("Vaqt davrlari", fontsize=12)
plt.ylabel("Qiymatlar", fontsize=12)
plt.legend()

plt.show()