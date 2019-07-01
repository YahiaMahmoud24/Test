import matplotlib.pyplot as plt
import numpy as np
########################## Part 1 ##########################
'''
import csv
## plt is a shortened version of matplotlib.pyplot

x = []
y = []
with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',') ## delimiter is the separator of two pieces of data
    for row in plots:
        x.append(int(row[0])) ##csv.reader reads the data in the .txt file and puts it into strings
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded From Sensors')
    '''

x, y = np.loadtxt('example.txt', delimiter = ',', unpack = True)  ## delimiter is the separator of two pieces of data
## unpack sorts each set into x and y
plt.plot(x,y, label='Loaded From Sensors')


# creating legends, titles, and lables
# Titles and labels
plt.xlabel('x') ## labels x-coordinate
plt.ylabel('y') ## labels y-coordinate
plt.title('A Very Interesting Title\nUwU') ## creates a title
# Legends
plt.legend()
plt.show() ## initiates graphics window