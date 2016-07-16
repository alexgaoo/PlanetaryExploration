import numpy as np

class PlanetaryExploration()
    def __init__(self,
                 term_r = 100,
                 nonterm_r = -1,
                 discount = .75)
        
        self.actions = np.array([-1,0,1])
        
        self.n_actions = 4
        self.model_dims = 
        
        

    def transition(self, a): 
        # transitions the simulator by performing the action a
        

    def reward(self):
        # returns the reward R(s,a) where s is the state before calling act, and a is the action passed to act
        r = 
        if self.episode_over:
            r = -
            
        

    def get_screenshot(self):
        # returns the current state of the system
        
       

    def episode_over(self):
        # returns true if the current state is terminal, false otherwise
        # checks if all sites are explored
        

    def reset_episode(self):
        # reinitializes the current state and reward
        
