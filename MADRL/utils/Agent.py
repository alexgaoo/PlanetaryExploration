using numpy as np

#################################################################
# Implements the Single 2D Agent Dynamics
#################################################################

class Agent():
	def __init__(self, xs, ys, matrix_map, seed = 1):

		self.random_state = np.random.RandomState(seed)

		self.xs = xs
		self.ys = ys

		self.eactions = [0, 	# move left
				 1, 	# move right
				 2, 	# move up
				 3,	# move down
				 4]	# stay

		self.motion_range = [[-1, 0],
				           [1, 0],
				           [0, 1],
				           [0, -1],
				           [0, 0]]

		self.current_pos  = np.zeros(2, dtype = np.int32)
		self.last_pos = np.zeros(2, dtype = np.int32)
		self.temp_pos = np.zeros(2, dtype = np.int32)

		self.map_matrix = map_matrix

		self.terminal = False

#################################################################
# Dynamics Functions
#################################################################

	def  step(self, a):
		cpos = self.current_pos
		lpos = self.last_pos

		tpos = self.temp_pos





	def get_state(self):
		return self.current_pos

