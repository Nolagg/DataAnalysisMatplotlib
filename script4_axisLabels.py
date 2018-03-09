import codecademylib
from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

#Let's modify the axes to zoom in a bit more on our line chart. Use plt.axis to modify the axes so that the x-axis goes from 0 to 12, and the y-axis goes from 2900 to 3100.
plt.axis([0, 12, 2900, 3100])

plt.show()