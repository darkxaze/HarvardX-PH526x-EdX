#%%
########## not complete ##############
import numpy as np
import random as random
import matplotlib.pyplot as plt

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2-p1, 2)))
p1 = np.array([1,1])
p2 = np.array([4,4])
print("distance from point 1 to point 2:", distance(p1,p2))

def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1 
        else:
            vote_counts[vote] = 1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
        # print(vote, counts)
    # print("winners:", winners)    
    # return vote_counts
    return random.choice(winners)

votes = [1,2,3,1,2,3,1,2,3,2,2,2,3,3,3]
winner = majority_vote(votes)
# print("vote_counts:", vote_counts)
print("winner:", winner)

# print("max of vote_counts:", max(vote_counts))
# print("max of vote_counts keys:", max(vote_counts.keys()))
# print("max of vote_counts values:", max(vote_counts.values()))

# loop over all points
    # compute the distance between point p and all the other points
# sort distances and return those k points that are closest to point p

#%%
distances = np.zeros(points.shape[0])
for i in range(len(distances)):
    distances[i] = distance(p, points[i])

points  =  np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5, 2])

import matplotlib.pyplot as plt
print(plt.plot(points[:,0], points[:,1], "ro"))
print(plt.plot(p[0],p[1], "bo"))
plt.axis([0.5, 3.5, 0.5, 3.5])