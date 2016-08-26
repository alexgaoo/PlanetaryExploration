class AgentLayer():

    # constructor
    def __init__(self,
                 xs, # x size of map
                 ys, # y size of map
                 agents):# list of agents
        """
        Each agent must support:
        - move(action)
        - current_position()
        - nactions()
        - set_position(x, y)
        """

        self.agents = agents
        self.nagents = len(agents)
        self.global_state = np.zeros((xs, ys), dtype=np.int32)

    def n_agents(self):
        return self.nagents

    def move_agent(self, agent_idx, action):
        return self.agentsagent_idx].step(action)

    def set_position(self, agent_idx, x, y):
        self.agents[agent_idx].set_position(x,y)

    def get_position(self, agent_idx):
        """
        Returns the position of the given agent
        """
        return self.agents[agent_idx].current_position()

    def get_nactions(self, agent_idx):
        return self.agents[agent_idx].nactions()

    def remove_agent(self, agent_idx):
        # idx is between zero and nagents
        self.agents.pop(agent_idx)
        self.nagents -= 1

    def get_state_matrix(self):
        """
        Returns a matrix representing the positions of all agents
        Example: matrix contains the number of algents at give (x,y) position
        0 0 0 1 0 0 0
        0 2 0 2 0 0 0
        0 0 0 0 0 0 1
        1 0 0 0 0 0 5
        """
        gs = self.global_state
        gs.fill(0)
        for agent in self.agents:
            x, y = agent.current_position()
            gs[x,y] += 1    
        return gs

    def get_state(self):
        pos = np.zeros(2*len(self.agents))
        idx = 0
        for agent in self.agents:
            pos[idx:(idx+2)] = agent.get_state()
            idx += 2
        return pos
