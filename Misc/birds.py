import datetime
import pandas as pd 
import numpy as np 
import bokeh as bokeh
from math import *
from random import *
import matplotlib.pyplot as plt

birddata = pd.read_csv("bird_tracking.csv")
# print("info on bird data:", birddata.info)
# print("head of bird data:", birddata.head())
# print("tail of bird data:", birddata.tail())

# ix = birddata.bird_name == "Eric"
# x,y = birddata.longitude[ix],birddata.latitude[ix]

# plt.figure(figsize=(7,7))
# plot1 = plt.plot(x,y,".")

# # comment this code after ran once
# # plt.savefig("plot1.pdf")

bird_names = pd.unique(birddata.bird_name)
# print("bird_names",bird_names)

# plt.figure(figsize=(7,7))
# for bird_name in bird_names:
#     ix = birddata.bird_name == bird_name
#     x,y = birddata.longitude[ix],birddata.latitude[ix]
#     plt.plot(x,y,".", label = bird_name)
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.legend(loc="lower right")
# # comment this code after ran once
# # plt.savefig("plot1**.pdf")

#  # wrong code
# ix = birddata.bird_name == "Eric"
# speed  = birddata.speed_2d[ix]
# print(plt.hist(speed))

ix = birddata.bird_name == "Eric"
speed  = birddata.speed_2d[ix]
ind = np.isnan(speed)
# print(~ind)
Eric = plt.hist(speed[~ind])

# comment this code after ran once
# plt.savefig("eric.pdf")

# alternate approach  with pandas
birddata.speed_2d.plot(kind = 'hist', range = [0,30])
plt.xlabel("2D speed");
# comment this code after ran once
# plt.savefig("Eric*withPD.pdf")

# print("columns", birddata.columns)

# print("timestamps")
# print(birddata.date_time[:3])

date_str = birddata.date_time[0]
print("date str", date_str)
print("type of date str", type(date_str))
print("date str without universial encoding", date_str[:-3])

# datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H: %M:%S")
# code not finished
