import State

class Policy:

    mappingList = []

    def add_optimized_policy(self, state, action):
        #add the optimized policy found by the algorithm with an immutable tuple (state,action)
        mapped = False
        state_hash = state.getHash()
        if not self.mappingList:
            self.mappingList.append([state_hash, action])
            mapped = True
        else:
            for pol in self.mappingList:
                if state_hash in pol:
                    pol[1] = action
                    mapped = True
                    break
            if not mapped:
                self.mappingList.append([state_hash, action])


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





