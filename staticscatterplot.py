import matplotlib.pyplot as plt

# Sample static data
x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 13, 17, 20, 22]

# Create scatter plot
plt.scatter(x, y, color='green', marker='o')

# Add title and labels
plt.title("Simple Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

# Show grid (optional)
plt.grid(True)

# Display the plot
plt.show()