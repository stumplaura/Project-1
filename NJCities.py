#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 21:46:14 2022

@author: morganstump
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style as sty
import csv
#READ FILE AND INSERT SPECIFIC COLUMNS
data = pd.read_csv("NJCrime.csv", index_col=0)
df = pd.DataFrame(data, columns= ['Total Crime', 'Population', 'Crime Ratio'])
# this data will show top 5 and bottom 5 of all columns. It will help
#test the hypothesis; it will also be good to look at when comparing the
#accuracy individual crime/pop ratio and the avg crime ratio
sample = df[df.columns[:3]]
print(sample)
#prints the 3 columns into separate CSV file
for line in df:
        df.to_csv('NJCrimeDataFiles.csv')
#CALCULATE CRIME RATIO AND PERCENTAGE
#entire column divided by number of rows/entries
avg = sum(df['Crime Ratio']/488)
#prints the average of all the rows crime/population
print("\nThe average Crime Ratio is ", (avg))
#ANSWER: 0.03620254888319668
#makes the average into a percentage per populational crime
print("The average Crime Percentage per populational crime is ", (avg * 100), "%")
#ANSWER: 3.6202548883196677%
#CREATE A TABLE WITH X VALUE: CRIME AND Y: VALUE CRIME RATIO
#Scatter
y = df['Crime Ratio']
x = df['Total Crime']
plt.title('New Jersey Crime')
plt.ylabel('Crime Ratio')
plt.xlabel('Total Crime')
plt.scatter(x, y,marker='+')
plt.show()
#CONCLUSION BASED OFF OF SCATTER PLOT TABLE:
#The crime ratio between total crime divided by total population
#remains fairly stagnant between all cities besides one outlier
# BAR GRAPH (preferred scatter plot visual)
# sty.use('ggplot')
# x1 = df['Population']
# y1 = df['Total Crime']
# x2 = df['Crime Ratio']
# y2 = df['Total Crime']
# plt.title('Crime')
# plt.ylabel('Total Crime')
# plt.xlabel('Crime Ratio')
# plt.bar(x1, y1, color='blue', align='center')
# plt.bar(x2, y2, color='red', align='center')
# plt.show()