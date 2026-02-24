import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# create a circle
circle = plt.Circle((0, 5), 0.5)
ax.add_patch(circle)

def update(x):
    circle.center = (x, 5)   # move circle horizontally
    return circle,

ani = FuncAnimation(fig, update, frames=range(0, 10), interval=500)

plt.show()
