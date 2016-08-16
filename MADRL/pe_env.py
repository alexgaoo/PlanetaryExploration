import glob
import os
from os.path import join
from subprocess import call

import numpy as np
import scipy.spatial.distance as ssd
from gym import spaces

from .utils import agent_utils
from .utils.AgentLayer import AgentLayer
from .utils.Controllers import RandomPolicy

#################################################################
# Implements a Multi Agent Planetary Exploration Problem in 2D 
#################################################################


class PlanetaryExploration():
	def __init__(self, map_matrix, n_agents = 3, site_reward = 1, noterm = -0.1, term = 10):
		self.n_agents = n_agents
		self.site_reward = site_reward
		self.noterm = noterm
		self.term = term

		agents = agent_utils.create_agents(self.n_agents, map_matrix)

	@property	
	def action_space(self):
		return spaces.Discrete()	

	@property
    	def observation_space(self):
              	return spaces.Box(###)
  

	def reset(self):

		return o


	def step(self, actions):
		r = self.reward


		for i, a in enumerate(actions):
            		agent_layer.move_agent(i, a)



		done = self.is_terminal
		info = None
		return o, r, done, info	

	def reward(self):
		r = joint_reward() 
		return r

	def joint_termr(self):
		r_joint = self.term * 

	def join_notermr(self):
		r_joint = self.noterm * 

             def is_terminal(self):
             	if 







