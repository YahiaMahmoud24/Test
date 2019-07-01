import matplotlib.pyplot as plt
 ## plt is a shortened version of matplotlib.pyplot
days = [1,2,3,4,5,6,7]

temp = [17, 25, 34, 38, 4, 15, 27]
moist = [79.97, 11.56, 2.97, 0.18, 1.45, 0.20, 0.09]
lumin = [24.6, 40.6, 17.4, 20.5, 23.4, 36.5, 12.2]

plt.plot([],[], color = 'm', label = 'Temperature', linewidth = 5)
plt.plot([],[], color = 'c', label = 'Moisture', linewidth = 5)
plt.plot([],[], color = 'r', label = 'Luminance', linewidth = 5)

plt.stackplot(days, temp, moist, lumin, colors =['magenta', 'cyan', 'red'])
# creating legends, titles, and lables
# Titles and labels
plt.xlabel('x') ## labels x-coordinate
plt.ylabel('y') ## labels y-coordinate
plt.title('A Very Interesting Title\nUwU') ## creates a title
# Legends
plt.legend()
plt.show() ## initiates graphics window