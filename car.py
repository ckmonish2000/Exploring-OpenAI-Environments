import gym
import matplotlib
env=gym.make('MountainCar-v0')
env.reset()

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE=[20] * len(env.observation_space.high)

done= False

while not done:
    action=2
    new_state,reward,done,_=env.step(action)
    env.render()
    print(new_state)
env.close()