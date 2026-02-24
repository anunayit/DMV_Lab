import matplotlib.pyplot as plt


labels = ['Apples', 'Bananas', 'Cherries', 'Oranges']
sizes = [30, 25, 20, 25]   # Fixed values


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("Fruit Distribution")

plt.show()
