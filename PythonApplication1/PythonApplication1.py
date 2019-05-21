from math import cos,radians
#Create a string with spaces proportional to a cosine of x in degrees
#def make_dot_string(x):
#    Rad = radians(x)    
#    numspaces = int(20 * cos(Rad) + 20)
#    st = ' ' * numspaces + 'o'
#    return st
#def main():
#    for i in range(0,1800,12):
#        s = make_dot_string(i)
#        print(s)
#main()
import numpy as np 
import matplotlib.pyplot as plt

def main():
    x = np.arange(0,radians(1800),radians(12))
    plt.plot(x,np.cos(x),'b')
    plt.show()
main()