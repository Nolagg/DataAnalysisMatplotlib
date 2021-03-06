import codecademylib
from matplotlib import pyplot as plt

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

# First, close all plots to make sure we have no lines already plotted that we’ve forgotten about
plt.close('all')

# Create a figure and plot word_length against years. This dataset represents the lengths of the winning words of the Scripps National Spelling Bee over 11 years. Save this figure in a file called 'winning_word_lengths.png'.
plt.figure(figsize=(6, 7))
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')

# On the next line, create a figure with 7 inches of width and 3 inches of height and plot power_generated against years. This dataset represents the power generated by nuclear plants in the United States over 11 years. Save this figure in a file called 'power_generated.png'
plt.figure(figsize=(3, 7))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')