import pickle

load_name = 'QLearningAgent_X_QTable'
with open(load_name, 'rb') as handle:
    Q = pickle.load(handle)
print(Q)

print("--------------------------------------------------------------------------------------------------------------")

load_name = 'QLearningAgent_O_QTable'
with open(load_name, 'rb') as handle:
    Q1 = pickle.load(handle)
print(Q1)
# print(f'\nQ-Table for {self.name} loaded as >{load_name}< B)\n')