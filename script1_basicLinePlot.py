#  Basic Line Plot I
#We are going to make a simple graph representing someone's spending on lunch over the past week. First, define two lists, days and money_spent, that contain the following integers:

# Days	Money Spent
# 0	10
# 1	12
# 2	12
# 3	10
# 4	14
# 5	22
# 6	24

# Plot days on the x-axis and money_spent on the y-axis using plt.plot
# Show the plot using plt.show().


import codecademylib
from matplotlib import pyplot as plt

days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]

plt.plot(days, money_spent)
plt.show()