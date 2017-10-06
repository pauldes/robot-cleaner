import State

class Policy:

    mappingList = []

    def add_optimized_policy(self, state, action):
        #add the optimized policy found by the algorithm with an immutable tuple (state,action)
        self.mappingList.append((state, action))

    def state_already_exists(self,new_state):
        for pol in self.mappingList:
            return new_state in pol

