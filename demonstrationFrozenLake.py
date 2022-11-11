# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:32:39 2022

Demonstration of the OpenAI Gym Library 
and the Fronzen Lake reinforcement learning environment

@author: Aleksandar Haber 

Website accompanying this code with background information
and theoretical explanations is given here:

https://aleksandarhaber.com/introduction-to-state-transition-probabilities-actions-and-rewards-with-openai-gym-reinforcement-learning-tutorial/

"""
import gym

env=gym.make("FrozenLake-v1")

# render the environment
env.render()

# observation space - states 
env.observation_space

# actions: left -0, down - 1, right - 2, up- 3
env.action_space

# reset the environment
env.reset()

#generate random action
randomAction= env.action_space.sample()
returnValue = env.step(randomAction)
# return value has the following form 
# (state, reward, Is it Terminal State?, {'prob': probability value of going to state})

env.render()

# perform deterministic step 0,1,2,3
returnValue = env.step(1)

env.render()





#transition probabilities
#p(s'|s,a) probability of going to state s' 
#          starting from the state s and by applying the action a

# env.P[state][action]
env.P[6][1] 
# output is a list having the following entries
# (transition probability, next state, reward, Is terminal state?)