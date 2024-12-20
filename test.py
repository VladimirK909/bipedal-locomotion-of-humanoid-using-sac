import gymnasium as gym
from stable_baselines3 import SAC
import os
import argparse


def test(env, path_to_model):

    model = SAC.load(path_to_model, env=env)

    obs = env.reset()[0]
    done = False
    extra_steps = 500
    while True:
        action, _ = model.predict(obs)
        obs, _, done, _, _ = env.step(action)

        if done:
            extra_steps -= 1

            if extra_steps < 0:
                break


if __name__ == '__main__':

    # Parse command line inputs
    parser = argparse.ArgumentParser(description='Test model')
    parser.add_argument('path_to_model')
    args = parser.parse_args()

    # Check if folder exists and test
    if os.path.isfile(args.path_to_model):
        gymenv = gym.make('Humanoid-v4', render_mode='human')
        test(gymenv, args.path_to_model)
    else:
        print(f'{args.test} not found.')
