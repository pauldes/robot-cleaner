import State
import random

from Simulator import pool_of_actions


class Policy:

    mappingList = []

    def add_optimized_policy(self, state, action):
        #add the optimized policy found by the algorithm with an immutable tuple (state,action)
        self.mappingList.append((state, action))

    def state_already_exists(self,new_state):
        for pol in self.mappingList:
            return new_state in pol

    def show_policy(self):
        for element in self.mappingList:
            print(str(element[0]), " =>", element[1])

    def random_policy(self):
        a = random.choice(pool_of_actions)
        return a

