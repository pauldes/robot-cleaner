import State
import random

from Simulator import pool_of_actions

class Policy:

    mappingList = []

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
            if element[0].getHash() == hash_state:
                return element[1]





