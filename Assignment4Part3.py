import math
import csv
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile
import numpy as np


# change mypath to your own directory
mypath = '/Users/joshwong/Desktop/BCIT/ACIT 1515/Assignment 4'

# create empty lists to store file names
filelist = []
csvfiles = []
xs = []
ys = []
yi = []
yq = []

# store all file names in directory to filelist
for f in listdir(mypath):
    if isfile(f) is True:
        x = f
        filelist.append(x)

# store all .csv files from filelist to csvfiles
for x in filelist:
    if '.csv' in x:
        csvfiles.append(x)

# loop through the .csv files
for x in csvfiles:
    try:
        infile = x
        outfile = 'graph'

        # parse data from .csv file
        with open('../Assignment 4/sort_time.csv', 'r') as csvfile:
            r = csv.reader(csvfile, delimiter=',')
            r = list(r)
            r.pop(0)
            data = r
            print(data)
            for i in range(len(data)):
                if i != '> 30 min':
                    xs.append(float(data[i][0]))
                    ys.append(float(data[i][1]))
                    yi.append(float(data[i][2]))
                    yq.append(float(data[i][3]))

                print(xs)

            plt.plot(xs, ys, color="r")
            plt.plot(xs, yi, color="g")
            plt.plot(xs, yq, color="b")

            plt.savefig('../Assignment 4/graph.png')
            plt.show()
            plt.close()

    except:
        print('All conversion done.')
