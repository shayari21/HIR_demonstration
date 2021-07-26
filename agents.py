import random
import pickle
import config as cfg

class Human():
    def __init__(self):
        self.name = "Human"

class RandomActionAgent():
    def __init__(self, name = "RandomActionAgent"):
        self.name = name

    def choose_action(self, possible_actions):
        action = random.choice(possible_actions)
        return action

class QLearningAgent:
    def __init__(self, name, epsilon = cfg.epsilon, learning_rate = cfg.learning_rate, discount_factor = cfg.discount_factor):
        self.name = name
        self.epsilon = epsilon
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.Q = {}
        self.last_board = None
        self.state_action_last = None
        self.q_last = 0

    def reset(self):
        self.last_board = None
        self.state_action_last = None
        self.q_last = 0

    def epsilon_greedy(self, state, possible_actions):
        state = tuple(state)
        self.last_board = state

        if random.random() < self.epsilon:
            action = random.choice(possible_actions)

        else:
            q_list = []
            for action in possible_actions:
                q_list.append(self.getQ(state,action))
            maxQ = max(q_list)

            if q_list.count(maxQ) > 1:
                maxQ_actions = [i for i in range(len(possible_actions)) if q_list[i] == maxQ]
                action_idx = random.choice(maxQ_actions)
            else:
                action_idx = q_list.index(maxQ)

            action = possible_actions[action_idx]

        self.state_action_last = (state, action)
        self.q_last = self.getQ(state , action)

        return action

    def getQ(self, state, action):
        return self.Q.get((state, action), 1.0)

    def updateQ(self, reward, state, possible_actions):
        q_list = []
        for action in possible_actions:
            q_list.append(self.getQ(tuple(state), action))

        if q_list:
            maxQ_next = max(q_list)
        else:
            maxQ_next = 0

        self.Q[self.state_action_last] = self.q_last + self.learning_rate * ((reward + self.discount_factor * maxQ_next) - self.q_last)

    def saveQtable(self):
        '''
        saves the Q-Table as a pickle file
        '''
        save_name = self.name + '_QTable'
        with open(save_name, 'wb') as handle:
            pickle.dump(self.Q, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print(f'\nQ-Table for {self.name} saved as >{save_name}<\n')

    def loadQtable(self): # load table
        '''
        loads the Q-Table from a pickle file
        '''
        load_name = self.name + '_QTable'
        with open(load_name, 'rb') as handle:
            self.Q = pickle.load(handle)
        print(f'\nQ-Table for {self.name} loaded as >{load_name}< B)\n')
