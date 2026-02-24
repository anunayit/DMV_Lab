import matplotlib.pyplot as plt

n = int(input("Enter number of values: "))

data = []

for i in range(n):
    value = int(input(f"Enter value : "))
    data.append(value)

plt.hist(data)
plt.show()
