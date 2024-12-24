from stable_baselines3 import SAC
import gymnasium as gym
import os
import time
import argparse


def train(env, tag, model_dir, log_dir):
    '''
    env - gymnasium environment to be trained on
    tag - name tag for experiment, included in folder names
    model_dir - directory where the trained models are saved
    log_dir - directory where the Tensorboard logs are saved
    '''

    # Defining the model and its params <CHANGEABLE>
    model = SAC('MlpPolicy', env, 0.0006, tau=0.001,
                batch_size=512, train_freq=2,
                verbose=1, tensorboard_log=log_dir)

    TIMESTEPS = 25000  # time steps at which model is saved
    iters = 0
    while True:
        iters += 1
        model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)
        model.save(f"{model_dir}/{tag}_{TIMESTEPS*iters}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('tag', help='specify experiment tag')
    args = parser.parse_args()

    # Create directories
    model_dir = f"models_{args.tag}"
    log_dir = f"logs_{args.tag}"
    os.makedirs(model_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)

    # Train
    print(time.time())
    gymenv = gym.make('Humanoid-v4', render_mode=None)
    train(gymenv, args.tag, model_dir, log_dir)
