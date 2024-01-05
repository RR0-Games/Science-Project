import matplotlib.pyplot as plt
import numpy as np

# Define the x and y coordinates of the magnets
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 0, 0, 0, 0])

# Define the magnetization of the magnets
magnetization = np.array([1, 2, 3, 2, 1])

# Define the time steps
t = np.linspace(0, 10, 100)

# Define the animation function
def animate(i):
    plt.clf()
    plt.plot(x, y, 'ko')
    plt.plot(x, y + magnetization * np.sin(i * t), 'r-')
    plt.xlim(-1, 5)
    plt.ylim(-4, 4)
    plt.xlabel('Distance')
    plt.ylabel('Magnetic Field')
    plt.title('Temporary Magnets Animation')

# Create the animation
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(plt.gcf(), animate, frames=100, interval=50)

# Save the animation
ani.save('temporary_magnets_animation.mp4', writer='ffmpeg', fps=30)
