import random
from State import State
from Simulator import Simulator
from Simulator import pool_of_actions
from Policy import Policy


class DynamicProgramming:
    # actions dictionnary
    states = []
    initial_state = State(State.battery_capacity, [0, 0], [0, 0], [[1] * State.sizeX] * State.sizeY )
    states_hash = []

    mode = 1

    epsilon = 0.01
    discounted_factor = 0.99
    policy = Policy()

    def generate_all_room_state(self, b, pRob, pBas):

        nbcombi = pow(2, State.sizeX * State.sizeY)  # room size ^2
        lroom = State.sizeX * State.sizeY  # room size


        n = 0

        while n < nbcombi:  # generate all combi possible
            roomG = [[0] * State.sizeX] * State.sizeY  # room
            binary = [0] * lroom  # list of all cases in room
            nb = str(bin(n))  # count in binary
            nb = nb[2:]  # get only the numerical part

            i = 0
            while i+len(nb) < lroom:
                binary[i] = 0  # add 0 while the number has a length under the length of the nb of room's case
                i += 1
            for j in range(0, len(nb)):
                binary[i+j] = int(nb[j])  # add the number
            # binary completed

            offset = 0
            for line in range(0, State.sizeY):
                roomG[line] = binary[offset: offset+State.sizeX]  # cut the binary list in Y line of X column
                offset += State.sizeX

            ns = State(b, pRob, pBas, roomG)
            self.states.append(ns)

            self.states_hash.append(ns.getHash())

            n += 1


    def generate_all_states(self):
        for b in range(0, State.battery_capacity+1):
            for prx in range(0, State.sizeX):
                for pry in range(0, State.sizeY):
                    for pbx in range(0, State.sizeX):
                        for pby in range(0, State.sizeY):
                            self.generate_all_room_state(b, [prx, pry], [pbx, pby],)

    def find_index_of_new_state(self, news):
        news_hash = news.getHash()
        if news_hash in self.states_hash:
            return self.states_hash.index(news_hash)
        else:
            print("error : new state hash", news_hash, " not in states list")
            return None



    def pick_random_actions(self):
        return random.choice(pool_of_actions)

    def max_perf(self, q_s_a):
        indMax = 0
        valueMax = 0
        for i, v in enumerate(q_s_a):
            if v > valueMax :
                valueMax = v
                indMax = i

        return indMax,valueMax

    def infinite_normal(self, v_value, v_value_prime):
        max_diff = 0
        for i in range(0, len(self.states)):
            val = abs(v_value_prime[i]-v_value[i])
            if val > max_diff:
                max_diff = val
        return max_diff

    def main(self):
        sim = Simulator()
        self.generate_all_states()
        print(len(self.states))

        v_value = [-100] * len(self.states)  # the value at index i is the performance for the state i in states
        v_value_prime = [+100]*len(self.states)


        while self.infinite_normal(v_value, v_value_prime) >= self.epsilon:
            v_value_prime = v_value
            for ind_s, s in enumerate(self.states):

                q_s_a = [0]*len(pool_of_actions)
                # for each action
                for ind_a, a in enumerate(pool_of_actions):
                    r_s_a, p_sPrime_knowingSandA, s_prime = sim.simulate(s.copy(), a, 'Dynamic Programming')
                    q_s_a[ind_a] = r_s_a
                    if p_sPrime_knowingSandA and s_prime and len(p_sPrime_knowingSandA) == len(s_prime):
                        for i, p in enumerate(p_sPrime_knowingSandA):
                            ind_s_prime = self.find_index_of_new_state(s_prime[i])
                            if ind_s_prime is None:
                                break
                            q_s_a[ind_a] += self.discounted_factor * p * v_value_prime[ind_s_prime]
                # compute max value
                ind_a_max, v_value[ind_s] = self.max_perf(q_s_a)
                self.policy.add_optimized_policy(s.copy(), pool_of_actions[ind_a_max])

        print("performance: ", v_value)
        self.policy.show_policy()
        index_state_initial = self.find_index_of_new_state(self.initial_state)
        v_initial = v_value[index_state_initial]
        print("performance initial DP : ", v_initial)


if __name__ == "__main__":
    dp = DynamicProgramming()
<<<<<<< HEAD
    dp.main()
=======
    dp.main()
>>>>>>> origin/master
