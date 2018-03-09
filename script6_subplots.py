mport codecademylib
from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

#The command plt.subplot needs three arguments to be passed into it:
# The number of rows of subplots
# The number of columns of subplots
# The index of the subplot we want to create

# We have defined the lists months, temperature, and flights_to_hawaii for you. 
# Using the plt.subplot command, plot temperature vs months in the left box of a figure that has 1 row with 2 columns.
plt.subplot(1, 2, 1)
plt.plot(months, temperature, color='green')
plt.title('First Subplot')

# Plot flights_to_hawaii vs temperature in the same figure, to the right of your first plot. Add the parameter "o" to the end of your call to plt.plot to make the plot into a scatterplot, if you want!
plt.subplot(1, 2, 2)
plt.plot(flights_to_hawaii, temperature, color='purple')
plt.title('Second Subplot')


# Increase the spacing between horizontal subplots to 0.35 and the bottom margin to 0.2.
plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()