import codecademylib
from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]


# We have defined lists called time, revenue, and costs. Plot revenue vs time.
# Plot costs vs time on the same plot as the last line.
plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()