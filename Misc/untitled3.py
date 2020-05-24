import random
import matplotlib.pyplot as plt  
import numpy as np

ys = []

for rep in range(5):
	y = 0
	for k in range(10):
		x = random.choice(range(1,7))
		y = y+x
	ys.append(y)
