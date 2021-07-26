summary_dir = 'summary'
num_episodes = 500000
display = True

# exploration-exploitation trade-off factor
epsilon = 0.25  # must be a real number between (0,1)

# learning-rate
learning_rate = 0.3  # must be a real number between (0,1)

# discount-factor
discount_factor = 0.9  # must be a real number between (0,1)

WorkerRobot_QLearningAgent_name = 'QLearning_Robot'

def display_board(board, action, workerID, worker1, worker2, reward, done, possible_actions, training=True,
                  episode_reward_worker1=None, episode_reward_worker2=None):

    print('\n')
    print(board)

    worker = worker1.name if workerID else worker2.name
    print(f'{worker} takes action {action}, gets reward {reward}. Done -> {done}')
    if episode_reward_worker1 is not None:
        print(f'episode_reward_worker1 -> {episode_reward_worker1}')
        print(f'episode_reward_worker2 -> {episode_reward_worker2}')
    if reward == -1:
        print("New action called")
    elif reward == 1:

        print("Process complete!")
    elif reward == -10:
        print("Product didn't assemble successfully.")
