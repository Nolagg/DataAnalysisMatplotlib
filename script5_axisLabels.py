import codecademylib
from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
# Label the x-axis 'Time'.
plt.xlabel('Time')
# Label the y-axis 'Dollars spent on coffee'.
plt.ylabel('Dollars spent on coffee')
# Add the title 'My Last Twelve Years of Coffee Drinking'.
plt.title('My Last Twelve Years of Coffee Drinking')
plt.show()