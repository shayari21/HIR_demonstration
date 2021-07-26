import sys, os, shutil, pdb, random
from tqdm import tqdm

def q(text=''):
    print(f'>{text}<')
    sys.exit()


from environment import Workspace
from agents import QLearningAgent, Human
import config as cfg
from config import display_board

env = Workspace()
worker1 = QLearningAgent(name=cfg.WorkerRobot_QLearningAgent_name)
worker1.loadQtable()  # load the learnt Q-Table
worker1.epsilon = 0  # greedy actions only, 0 exploration

player2 = Human()

replay = True
while replay:

    done = False  # the episode goes on as long as done is False

    playerID = False #random.choice([True, False])  # True means worker1

    while not done:
        if playerID:
            action = worker1.epsilon_greedy(env.board, env.possible_actions())
        else:
            print(f'\nPossible Actions: {env.possible_actions()}')
            action = int(input('Select an action ! '))

        reward, done = env.step(playerID, action)

        display_board(env.board, action, playerID, worker1, player2, reward, done, env.possible_actions(),
                      training=False)

        playerID = not playerID  # switch turns

    replay = input('\nContinue ? [y/n] ')
    if replay.lower() == 'y':
        env.reset()
        worker1.reset()
        print('\n-----------------------------NEW PROCESS-----------------------------')

    elif replay.lower() == 'n':
        replay = False