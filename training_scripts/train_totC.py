from stable_baselines3 import SAC
import gymnasium as gym
import os
import argparse


def train(env, tag, model_dir, log_dir):
    '''
    env - gymnasium environment to be trained on
    tag - name tag for experiment, included in folder names
    '''

    TIMESTEPS = 25000  # time steps at which model is saved
    iters = 0

    while True:
        policy_kwargs = dict(net_arch=[512, 512, 512])
        lr = 0.0006 if iters <= 24 else 0.0003

        # Defining the model and its params <CHANGEABLE>
        model = SAC('MlpPolicy', env, lr, ent_coef='auto_0.4',
                    batch_size=512, train_freq=3, policy_kwargs=policy_kwargs,
                    verbose=1, tensorboard_log=log_dir)

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
    gymenv = gym.make('Humanoid-v4', render_mode=None)
    train(gymenv, args.tag, model_dir, log_dir)
