import matplotlib.pyplot as plt

n = int(input("Enter number of bars: "))

x = []
y = []

for i in range(n):
    label = input(f"Enter label {i+1}: ")
    value = int(input(f"Enter value for {label}: "))
    x.append(label)
    y.append(value)

plt.bar(x, y)
plt.show()
