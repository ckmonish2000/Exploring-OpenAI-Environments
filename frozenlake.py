import gym 
import numpy as np
import random
import time

env=gym.make('FrozenLake-v0')

#number of rows in the table = state space
#number of column in the table = action space

action_space_size=env.observation_space.n
state_space_size=env.action_space.n

q_table=np.zeros((state_space_size,action_space_size))
print(q_table)

num_episodes=10000
num_steps_per_episode=100


# exploration and exploitation rate calculation
exploration_rate=1
min_exploration_rate=0.01
max_exploration_rate=1
exploration_decay_rate=0.001







