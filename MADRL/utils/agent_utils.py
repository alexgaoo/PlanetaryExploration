import numpy as np

from .Agent import Agent

#################################################################
# Implements utility functions for multi-agent DRL
#################################################################


def create_agents(nagents, map_matrix):
	"""
	Initializes the agents on a map (map_matrix)
	-nagents: the number of agents to put on the map
	"""
	xs, ys = map_matrix.shape
	agents = []
	for i in xrange(nagents):
	    xinit, yinit = (0, 0)
	    agent = TwoDAgent(xs, ys, map_matrix)
	    agent.set_position(xinit, yinit)
	    agents.append(agent)
	return agents

def set_agents(agent_matrix, map_matrix):
	# check input sizes
	if agent_matrix.shape != map_matrix.shape:
	    raise ValueError("Agent configuration and map matrix have mis-matched sizes")

	agents = []
	xs, ys = agent_matrix.shape
	for i in xrange(xs):
	    for j in xrange(ys):
	        n_agents = agent_matrix[i, j]
	        if n_agents > 0:
	            agent = TwoDAgent(xs, ys, map_matrix)
	            agent.set_position(i, j)
	            agents.append(agent)
	return agents