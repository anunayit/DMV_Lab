import matplotlib.pyplot as plt
import numpy as np
x_input = input("Enter X coordinates (separated by spaces): ")
y_input = input("Enter Y coordinates (separated by spaces): ")
try:
    x_data = np.array([float(i) for i in x_input.split()])
    y_data = np.array([float(i) for i in y_input.split()])

    if len(x_data) != len(y_data):
        print("Error: X and Y must have the same number of elements.")
    else:
        plt.figure(figsize=(8, 6))
        plt.scatter(x_data, y_data, color='purple', s=80, edgecolor='white', alpha=0.8)

        plt.title("User-Defined Scatter Plot", fontsize=14)
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.grid(True, linestyle=':', alpha=0.5)
        plt.show()

except ValueError:
    print("Error: Please enter only numbers separated by spaces.")