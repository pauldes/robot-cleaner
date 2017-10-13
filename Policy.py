import State
import random

from Simulator import pool_of_actions

class Policy:

    mappingList = []
    qLearning_policy = dict()

    def add_optimized_policy(self, state, action):
        #add the optimized policy found by the algorithm with an immutable tuple (state,action)
        hash = state.getHash()
        exist = False
        for element in self.mappingList:
            if hash in element:
                element[1] = action
                exist = True
                break
        if not exist:
            self.mappingList.append([hash, action])


    def state_already_exists(self,new_state):
        for pol in self.mappingList:
            return new_state in pol

    def show_policy(self):
        for element in self.mappingList:
            print(str(element[0]), " =>", element[1])

    def random_policy(self):
        a = random.choice(pool_of_actions)
        return a

    def find_the_action(self, state):
        hash_state = state.getHash()
        for element in self.mappingList:
            if element[0] == hash_state:
                return element[1]
# qlearning fonction
    def init_arbitrary_policy(self, state):
        # for each state a list with q-value corresponding to each action is associated
        q_s_a = [-200]*len(pool_of_actions)
        self.qLearning_policy[state.getHash()] = q_s_a

    def epsilone_greedy(self, state):
        # return the best action or arbitrary action if first times
        hash = state.getHash()
        if hash in self.qLearning_policy:
            qsa = self.qLearning_policy[hash]
            best_action, q_value_max = self.get_best_action(qsa)
            return best_action, qsa
        else :
            q_s_a = [0] * len(pool_of_actions)
            self.qLearning_policy[hash] = q_s_a
            return random.choice(pool_of_actions), q_s_a
            # arbitrary if all the value are equal the argmax will be move_left (first action in pool action)

    def update_optimized_policy(self, state, action, q_value):
        hash = state.getHash()
        if hash in self.qLearning_policy:
                ind_action = pool_of_actions.index(action)
                self.qLearning_policy[hash][ind_action] = q_value
        else:
            print("issue if updating then the state should exist in the dictionnary", hash)

    def get_best_action(self, q_s_a):
        indMax = 0
        valueMax = 0
        for i, v in enumerate(q_s_a):
            if v > valueMax:
                valueMax = v
                indMax = i

        return pool_of_actions[indMax], valueMax

    def get_performance(self, init):
        hash = init.getHash()

        if hash in self.qLearning_policy:
            best_action, perf = self.get_best_action(self.qLearning_policy[hash])
            return perf
        else:
            print('issue')
