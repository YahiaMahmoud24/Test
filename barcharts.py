import matplotlib.pyplot as plt
 ## plt is a shortened version of matplotlib.pyplot
x1 = int(input('enter your first x point'))
x2 = int(input('enter your second x point'))
x3 = int(input('enter your third x point'))
y1 = int(input('enter your first y point'))
y2 = int(input('enter your second y point'))
y3 = int(input('enter your third y point'))
x = [x1,x2,x3]
x2 = [x1+3, x2+5, x3+16] ## random additions, treat it as another set of points
y = [y1,y2,y3]
y2 = [y1-5,y2*2,y3**0.5]
plt.plot(x, y, label = 'First line') ##x and y are arguments
plt.plot(x2, y2, label  = 'Second Line')
## creating legends, titles, and lables
# Titles and labels
plt.xlabel('TiMe') ## labels x-coordinate
plt.ylabel('Important variable') ## labels y-coordinate
plt.title('A Very Interesting Title\nUwU') ## creates a title
# Legends
plt.legend()
plt.show() ## initiates graphics window