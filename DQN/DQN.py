import chainer
import chainer.functions as F
import chainer.links as L
from chainer import cuda, Function, gradient_check, Variable, optimizers, serializers, utils
from chainer import Link, Chain, ChainList

class CarNet(Chain):

    def __init__(self):
        super(CarNet, self).__init__(
            l1=F.Linear(2, 20), # 2 dimensional state space 
            bn1=L.BatchNormalization(20),
            l2=F.Linear(20, 10),
            bn2=L.BatchNormalization(10),
            lout=F.Linear(10, 3) # 3 output actions
        )
        # need this variable for batch normalization and dropout
        self.train = True
        # init avg_var to prevent divide by zero during first forward pass in batch norm
        self.bn1.avg_var.fill(0.1),
        self.bn2.avg_var.fill(0.1),


    def __call__(self, state, a):
        # Chimp passes in actions by defult if requested, not used here
        h = F.relu(self.l1(state))
        h = self.bn1(h, test=not self.train)
        h = F.relu(self.l2(h))
        h = self.bn2(h, test=not self.train)
        output = self.lout(h)
        return output
    
settings = {

    # agent settings
    'batch_size' : , # size of minibatch
    'print_every' : , # frequency of text output
    'save_dir' : 'results/planetary_exploration', # everything is saved here
    'iterations' : 2001, # length of training (low value as an example)
    'eval_iterations' : 100, # length of evaluation simulation
    'eval_every' : 1000, # frequnecy of evaluation simulation
    'save_every' : 20000, # frequency of network saving
    'initial_exploration' : 50000, # number of trainstions initally in reaply memory
    'epsilon_decay' : 0.000001, # subtract from epsilon every step
    'eval_epsilon' : 0, # epsilon used in evaluation, 0 means no random actions
    'epsilon' : 1.0,  # Initial exploratoin rate
    'history_sizes' : (1, 0, 0), # sizes of histories to use as nn inputs (s, a, r)
    'model_dims' : (2,),

    # simulator settings
    'viz' : False, # no visualization (used in Atari)

    # replay memory settings
    'memory_size' : 100000,  # size of replay memory

    # learner settings
    'learning_rate' : 0.00001, # learning rate used by the optimizer
    'discount' : 0.95, # discount rate for RL
    'clip_err' : False, # clip gradients
    'clip_reward' : False, # value to clip reward values to
    'target_net_update' : 1000, # frequnecy of target net updates
    'optim_name' : 'ADAM', # currently supports "RMSprop", "ADADELTA", "ADAM" and "SGD"'
    'gpu' : False, # not using GPU
    'reward_rescale': False, # rescale rewards to [0,1]
    'decay_rate' : 0.99, # decay rate for RMSprop, otherwise not used

     # random number seeds
    'seed_general' : 1723,
    'seed_simulator' : 5632,
    'seed_agent' : 9826,
    'seed_memory' : 7563

    }