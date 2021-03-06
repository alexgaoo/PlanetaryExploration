from __future__ import absolute_import, print_function

import argparse
import json

import tensorflow as tf

import gym
import rltools.algos.policyopt
import rltools.log
import rltools.util
from pe_env import PlanetaryExploration
from utils.Map import 
from rltools.samplers.serial import SimpleSampler, ImportanceWeightedSampler, DecSampler
from rltools.baselines.linear import LinearFeatureBaseline
from rltools.baselines.mlp import MLPBaseline
from rltools.baselines.zero import ZeroBaseline
from rltools.policy.categorical import CategoricalMLPPolicy, GaussianMLPPolicy

SIMPLE_POLICY_ARCH = '''[
        {"type": "fc", "n": 32},
        {"type": "nonlin", "func": "tanh"},
        {"type": "fc", "n": 32},
        {"type": "nonlin", "func": "tanh"}
    ]
    '''
SIMPLE_VAL_ARCH = '''[
        {"type": "fc", "n": 32},
        {"type": "nonlin", "func": "tanh"},
        {"type": "fc", "n": 32},
        {"type": "nonlin", "func": "tanh"}
    ]
    '''


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--env', type=str

    args = parser.parse_args()

    # init environment
    env = PlanetaryExploration

    # init policy network
    policy = CategoricalMLPPolicy(env.observation_space,
                                  env.action_space,
                                  hidden_spec=args.policy_hidden_spec,
                                  enable_obsnorm=True,
                                  tblog=args.tblog,
                                  varscope_name='pursuit_catmlp_policy')

    # init baseline
    baseline = MLPBaseline(env.observation_space,
                           args.baseline_hidden_spec,
                           True,
                           True,
                           max_kl=args.vf_max_kl,
                           damping=args.vf_cg_damping,
                           time_scale=1. / args.max_traj_len,
                           varscope_name='pursuit_mlp_baseline')

    # init sampler
    sampler_cls = DecSampler
    sampler_args = dict(max_traj_len=args.max_traj_len,
                        batch_size=args.batch_size,
                        min_batch_size=4,
                        max_batch_size=64,
                        batch_rate=40,
                        adaptive=False)

    # init TRPO step function
    step_func = rltools.algos.policyopt.TRPO(max_kl=args.max_kl)

    # init optimizer
    popt = rltools.algos.policyopt.SamplingPolicyOptimizer(
            env=env,
            policy=policy,
            baseline=baseline,
            step_func=step_func,
            discount=args.discount,
            gae_lambda=args.gae_lambda,
            sampler_cls=sampler_cls,
            sampler_args=sampler_args,
            n_iter=args.n_iter)

    # initialize logger
    argstr = json.dumps(vars(args), separators=(',', ':'), indent=2)
    rltools.util.header(argstr)
    log_f = rltools.log.TrainingLog(args.log, [('args', argstr)])

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        popt.train(sess, log_f, args.save_freq)


if __name__ == '__main__':
    main()