# YOU HAVE BEEN HACKED BY NICK
# SURRENDER NOW OR YOU WILL
# BE TURNED IN FOR COUNTERFEIT

import matplotlib.pyplot as plt
 ## plt is a shortened version of matplotlib.pyplot
popul_ages = [22, 33, 45, 64, 77, 84, 127, 12, 43, 45, 52, 45, 80, 52, 23, 57, 36, 70, 80, 23, 12, 34, 56, 78, 29]
#ids = [x for x in range(len(popul_ages))]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130] ## condenses data
plt.hist(popul_ages, bins, histtype = 'bar', rwidth = 0.8)
# creating legends, titles, and lables
# Titles and labels
plt.xlabel('x') ## labels x-coordinate
plt.ylabel('y') ## labels y-coordinate
plt.title('A Very Interesting Title\nUwU') ## creates a title
# Legends
plt.legend()
plt.show() ## initiates graphics window