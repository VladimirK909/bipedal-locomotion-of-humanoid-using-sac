# Achieving Stable Bipedal Locomotion of a Humanoid Robot using SAC within MuJoCo

This repository contains an implementation of stable bipedal locomotion control for humanoid robots using the **Soft Actor-Critic (SAC)** algorithm, simulated within the **MuJoCo** physics engine and trained using **Gymnasium** and **Stable Baselines 3**.

## Table of Contents
- [Acknowledgements](#acknowledgements)
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
    - [Training a New Model](#training-a-new-model)
    - [Visually evaluating a Pre-Trained Model](#visually-evaluating-a-pre-trained-model)
    - [Analytically evaluating a Pre-Trained Model](#analytically-evaluating-a-pre-trained-model)
- [Results](#results)

## Acknowledgements
The project showcased in this repository is part of my Bachelor's Thesis at the Faculty of Electrical Engineering and Information Technologies at the Ss. Cyril and Methodius University in Skopje. Parts of it were also done at the Faculty of Engineering Science at KU Leuven, Belgium.

The resources and services used in this work were provided by the VSC (Flemish Supercomputer Center), funded by the Research Foundation - Flanders (FWO) and the Flemish Government.

## Overview
Achieving stable bipedal locomotion (*aka walking with two legs*) is one of the key challenge in controlling a humanoid robot. One approach to solving this problem is to use the **Soft Actor Critic**  RL algorithm, which can be used to train the humanoid robot without the need for "traditional" manual modeling of the robot's dynamics.

This project explores the application of the SAC algorithm, a state-of-the-art reinforcement learning method, to overcome these challenges. The project uses a simulated humanoid environment to train and evaluate the locomotion control policy.

The purpose of this repository is the following:
1. To serve as a starting point for people who want to solve reinforcement learning problems similar to this one.
2. To be an illustrative example of how MuJoCo, Gymnasium, and Stable Baselines 3 can be integrated into a RL workflow.
3. To showcase the training results along with some pre-trained models and their parameters in order to facilitate future research into this problem. 

### Problem Definition:
That being said, the goal of this project is to **train a humanoid robot within a simulation environment using SAC** with the following characteristics:
- Stable bipedal locomotion (i.e. the robot doesn't fall)
- Walks on a flat surface
- Keeps moving in the required direction as fast as possible
- Does not change direction arbitrarily

## Features
- Implementation of the SAC algorithm using [Stable Baselines 3](https://stable-baselines3.readthedocs.io/en/master/modules/sac.html) and [Gymnasium](https://gymnasium.farama.org/environments/mujoco/humanoid/).
- Simulated environment using [MuJoCo](https://mujoco.org/).
- Pre-trained models for quick evaluation, along with gifs of the resultant humanoids.
- Visualization tools for analyzing training progress and walking behaviors.

## Getting Started

### Prerequisites
To use this repository, ensure you have the following:
- Python 3.8 or later
- Basic understanding of reinforcement learning and the SAC algorithm

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/VladimirK909/bipedal-locomotion-of-humanoid-using-sac.git
   cd bipedal-locomotion-of-humanoid-using-sac
   ```
2. **Install the required dependencies**:

    When installing the dependencies, you can try running the following command:
   ```bash
   pip install -r requirements.txt
   ```
    However, this might not always work as intended because of the MuJoCo installation, which is sometimes difficult to install depending on your system (especially if you are running Windows, like me).
    In that case, try running the following command taken from the [MuJoCo page](https://gymnasium.farama.org/environments/mujoco/) in the Gymnasium documentation:
    ```bash
    pip  install  gymnasium[mujoco]
    ```
    In any case, make sure you have Gymnasium, Stable Baselines 3, MuJoCo, and TensorBoard installed, and everything should work well.

## Repository Structure
```
.
├── models              # Some pre-trained models that can walk
├── gifs                # Gif videos of the pre-trained models
├── training_scripts    # Example training scripts with different params
├── test.py             # Script for visually evaluating a model
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Usage

### Training a New Model
To train a new SAC model, you need to create a training script `train.py` and set your training parameters (look at the `training_scripts/` folder in this repo for examples), and then run the following command:
```bash
python train.py tag
```
where `tag` is a specific nametag you ascribe to that particular set of parameters.

The training goes on indefinitely, and saves the model every `TIMESTEPS` time steps (look at the training scripts on line 19). You can monitor it through the terminal in real time and then you can shut it down manually by pressing Ctrl + C when you want to stop the training.

The script will create two folders, one called `models_tag` where the models are saved and one called `logs_tag` where the TensorBoard logs are saved.

### Visually evaluating a Pre-Trained Model
To visually evaluate a pre-trained model, run:
```bash
python test.py /path_to_model
```
This will open up a window where you can view the robot being controlled by the model and it will walk until it falls down or until you manually stop the simulation by exiting the vizualization window and pressing Ctrl + C.

### Analytically evaluating a Pre-Trained Model
You can use the saved logs for a model in the `logs_tag/` folder with **Tensorboard** to visualize all of the evaluation curves, such as the actor and critic losses and the mean reward per episode.
##
*The code in this project is inspired by and similar to this [Youtube video](https://youtu.be/OqvXHi_QtT0?si=nmVRt14LYDNvF8-l) by JohhnyCode. Watching it might elucidate some of the syntax if you are not able to directly follow it from this repository.*

## Results
The `models/` folder contains several pre-trained models that are the most promising in terms of achieving stable bipedal locomotion. They can all 'technically walk', that is to say they rarely fall and move forward, albeit a bit unnaturally at times. The `gifs/` folder contains short gifs of the models in action where you can see how they are able to walk.
Given the problem definition given above, the best model is `totB9`. It falls down very rarely, moves fast and keeps moving in a stable direction.

All of the parameters for the pre-trained models given here as well as the whole training process for this project can be viewed in this [table](https://docs.google.com/spreadsheets/d/1Sv9nNMe5b_wgv0WtCflXlFYwvArSOIMLqckGoUtySkU/edit?usp=sharing).

That being said, this is just a starting point and introducing more complexity in the simulation environment (for example adding an uneven floor instead of the perfectly flat one used here) will probably make the robot walk more naturaly. What is interesting to note here is that the gait of `TotB9` is similar to how people move in some dances or sports that require fast one-direction locomotion on a flat surface, such as fencing for example.
