# Thompson Sampling

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Thompson Sampling
import random
N = 10000
d = 10
ads_selected = list()
numbers_of_rewards_1 = [0 for _ in range(d)]
numbers_of_rewards_0 = [0 for _ in range(d)]

for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    numbers_of_rewards_1[ad] += dataset.values[n, ad] == 1
    numbers_of_rewards_0[ad] += dataset.values[n, ad] == 0

total_reward = sum(numbers_of_rewards_1)

# Visualising the results - Histogram
plt.hist(ads_selected)
plt.plot(numbers_of_rewards_1)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
