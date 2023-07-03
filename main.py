import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Set up the initial plot
line, = ax.plot([], [], 'r-', lw=2)

# Define the initialization function
def init():
    line.set_data([], [])
    return line,

# Define the update function for each frame
def update(frame):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(2 * np.pi * (x - 0.01 * frame))
    line.set_data(x, y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Display the animation
plt.show()
