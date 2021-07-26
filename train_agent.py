import random
from tqdm import tqdm
import matplotlib.pyplot as plt

import config as cfg
from agents import QLearningAgent
from environment import Workspace
from config import display_board

cfg.display = False
env = Workspace()
worker1 = QLearningAgent(name=cfg.WorkerRobot_QLearningAgent_name)

episodes = cfg.num_episodes
tot_rewards = []
for i in tqdm(range(episodes)):

    if cfg.display:
        print(f'TRAINING {str(i + 1).zfill(len(str(episodes)))}/{episodes}')

    episode_reward_worker1 = 0

    env.reset()
    worker1.reset()

    done = False

    workerID = True
    worker2 = None

    while not done:
        action = worker1.epsilon_greedy(env.board, env.possible_actions())
        reward, done = env.step(workerID, action)
        episode_reward_worker1 += reward
        worker1.updateQ(reward, env.board, env.possible_actions())
        if cfg.display:
            display_board(env.board, action, workerID, worker1,worker2, reward, done, env.possible_actions(), training=True)

    if episodes % 100 == 0:
        tot_rewards.append(episode_reward_worker1)
print(env.counter)
plt.plot(tot_rewards)
plt.show()
worker1.saveQtable()

















#
#
# import random
# from tqdm import tqdm
#
# import config as cfg
# from agents import QLearningAgent
# from environment import Workspace
# from config import display_board
#
# env = Workspace()
# worker1 = QLearningAgent(name=cfg.player0_QLearningAgent_name)
# worker2 = QLearningAgent(name=cfg.player0_QLearningAgent_name)
#
# episodes = cfg.num_episodes
#
# for i in tqdm(range(episodes)):
#
#     if cfg.display:
#         print(f'TRAINING {str(i + 1).zfill(len(str(episodes)))}/{episodes}')
#
#     episode_reward_worker1 = 0
#     episode_reward_worker2 = 0
#
#     env.reset()
#     worker1.reset()
#     worker2.reset()
#
#     done = False
#
#     workerID = random.choice([True, False])
#
#     while not done:
#         if workerID:
#             action = worker1.epsilon_greedy(env.board, env.possible_actions())
#         else:
#             action = worker2.epsilon_greedy(env.board, env.possible_actions())
#
#         reward, done = env.step(workerID, action)
#
#
#         if workerID:
#             episode_reward_worker1 += reward
#         else:
#             episode_reward_worker2 += reward
#
#         if cfg.display:
#             display_board(env.board, action, workerID, worker1, worker2, reward, done, env.possible_actions(),
#                           episode_reward_worker1, episode_reward_worker2)
#         if reward == 10:
#             if workerID:
#                 worker1.updateQ(reward, env.board, env.possible_actions())
#                 worker2.updateQ(-1 * reward, env.board, env.possible_actions())
#             else:
#                 worker2.updateQ(reward, env.board, env.possible_actions())
#                 worker1.updateQ(-1 * reward, env.board, env.possible_actions())
#
#         elif reward == -100:
#             if workerID:
#                 worker1.updateQ(reward, env.board, env.possible_actions())
#             else:
#                 worker2.updateQ(reward, env.board, env.possible_actions())
#
#         elif reward == 0:
#             if not workerID:
#                 worker1.updateQ(reward, env.board, env.possible_actions())
#             else:
#                 worker2.updateQ(reward, env.board, env.possible_actions())
#
#         workerID = not workerID

# worker1.saveQtable()
# worker2.saveQtable()
