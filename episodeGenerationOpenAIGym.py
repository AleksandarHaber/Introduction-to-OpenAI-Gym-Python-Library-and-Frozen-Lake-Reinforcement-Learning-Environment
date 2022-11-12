# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:29:24 2022

@author: Aleksandar Haber

This code demonstrates how to simulate episodes in OpenAI Gym

"""
import gym
import time
env=gym.make("FrozenLake-v1",render_mode='human')
env.reset()
env.render()
print('Initial state of the system')

numberOfIterations=30

for i in range(numberOfIterations):
    randomAction= env.action_space.sample()
    returnValue=env.step(randomAction)
    env.render()
    print('Iteration: {} and action {}'.format(i+1,randomAction))
    time.sleep(2)
    if returnValue[2]:
        break

env.close()    
