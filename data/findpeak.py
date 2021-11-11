#import library
from math import dist
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import neurokit2 as nk
from scipy.signal import find_peaks
import data3_10
from data3_10 import ppg

#mendefinisi x dan y array
#x= np.linspace(0,7244,7245) #data1_05
#x= np.linspace(0,3487,3488) #data1_10
#x= np.linspace(0,6468,6469) #data2_05
#x= np.linspace(0,3378,3379) #data2_10
#x= np.linspace(0,6642,6643) #data3_05
x= np.linspace(0,3372,3373) #data3_10
y= ppg
#menemukan puncak
peaks = find_peaks(y, height=525, threshold=0, distance=10)
height = peaks[1]['peak_heights']
peak_post= x[peaks[0]]

print("posisi titik puncak :", peak_post)


#menemukan nilai minimum
y2=y*-1
minima=find_peaks(y2)
min_pos=x[minima[0]]
min_height=y2[minima[0]]

#print titik puncak
peak_coordinate=peak_post
    #print(peak_coordinate)
#banyaknya puncak
    # print(len(peak_coordinate)) 
    #output 40
#data titik ke2 sampai 40
data1=peak_coordinate[1:]
#data titik ke1-39
data2=peak_coordinate[:-1]
#jarak antar puncak (pengurangan array)
distance= data1-data2
print("jarak antar puncak :", distance)   #selisih

average= distance/len(distance)

#minimum
#print(min(peak_post))
print("jarak terdekat :", min(distance))
print("jarak terjauh :", max(distance))
print("banyaknya peak :", len(distance))

#plotting
fig = plt.figure()
ax= fig.subplots()
ax.plot(x,y)
ax.scatter(peak_post, height, color='r', s=15, marker='D', label='puncak PPG')
ax.scatter(min_pos, min_height*-1, color='gold', s=15, marker='X', label='minimal')
ax.legend()
ax.grid()
plt.show()