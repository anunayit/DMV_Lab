import matplotlib.pyplot as plt

# Number of categories
n = int(input("Enter number of categories: "))

labels = []
sizes = []

# Taking user input
for i in range(n):
    label = input(f"Enter label for category {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    
    labels.append(label)
    sizes.append(value)

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add title
plt.title("Pie Chart (User Input)")

# Display chart
plt.show()