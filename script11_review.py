import codecademylib
from matplotlib import pyplot as plt

# Define three lists, x, y1, and y2 and fill them with integers. These numbers can be anything you want, but it would be neat to have them be actual metrics that you want to compare. This is a fun site you can look at to find example datasets to plot!
x = [ 1, 2, 3, 5, 8 ]
y1 = [ 20, 30 , 90, 22, 17 ]
y2 = [ 2, 7, 12, 5, 6]

# Plot y1 vs x and display the plot.
# On the same graph, plot y2 vs x (after the line where you plot y1 vs x)
# Make the y1 line a pink line and the y2 line a gray line. Give both lines round markers.
plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')
# Give your graph a title of “Two Lines on One Graph”, and label the x-axis ”Amazing X-axis” and y-axis ”Incredible Y-axis”.
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
# Give the graph a legend and put it in the lower right.
legend_labels = ['y1 Stuff', 'y2 Stuff']
plt.legend(legend_labels, loc=4)

plt.show