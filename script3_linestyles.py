import codecademylib
from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

#Plot revenue vs. time as a purple ('purple'), dashed ('--') line.
plt.plot(time, revenue, color='purple', linestyle='--')
#Plot costs vs. time as a line with the HEX color #82edc9 and square ('s') markers.
plt.plot(time, costs, color='#82edc9', marker='s')
plt.show()