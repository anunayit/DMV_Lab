import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

x = []
y = []

line, = ax.plot([], [])

def update(i):
    x.append(i)
    y.append(i)   # line grows (not straight at start)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=range(10), interval=500)

plt.show()
