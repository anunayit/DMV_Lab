import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))
x = []
y = []

for i in range(n):
    xi = int(input(f"Enter x{i+1}: "))
    yi = int(input(f"Enter y{i+1}: "))
    x.append(xi)
    y.append(yi)

plt.plot(x, y)
plt.show()
