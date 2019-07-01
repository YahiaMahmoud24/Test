# YOU HAVE BEEN HACKED BY NICK
# SURRENDER NOW OR YOU WILL
# BE TURNED IN FOR COUNTERFEIT

import matplotlib.pyplot as plt
 ## plt is a shortened version of matplotlib.pyplot
x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x, y, label = 'Bars 1', color = 'blue')
plt.bar(x2, y2, label = 'Bars 2', color = 'red')

# creating legends, titles, and lables
# Titles and labels
plt.xlabel('x') ## labels x-coordinate
plt.ylabel('y') ## labels y-coordinate
plt.title('A Very Interesting Title\nUwU') ## creates a title
# Legends
plt.legend()
plt.show() ## initiates graphics window
