import codecademylib
from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

# Start by using the subplot command to select the box in the top row (the one with the star in it).
plt.subplot(2, 1, 1)
# Plot straight_line vs x in this subplot you've selected.
plt.plot(straight_line, x)

# Now, use the subplot command to select the box in the first column of the second row (the one with a square in it). Plot parabola vs x in this box.
plt.subplot(2, 2, 3)
plt.plot(x, parabola)

# Now, use the subplot command to select the box in the second column of the second row (the one with a triangle in it). Plot cubic vs x in this box
plt.subplot(2, 2, 4)
plt.plot(x, cubic)

# Increase the spacing between horizontal subplots to 0.35 and the bottom margin to 0.2.
plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()