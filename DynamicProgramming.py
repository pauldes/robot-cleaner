import random
from State import State
from Simulator import Simulator
from Policy import Policy


class DynamicProgramming:
    # actions dictionnary
    actions = ['MOVE_LEFT', 'MOVE_RIGHT', 'MOVE_UP', 'MOVE_DOWN', 'VACUUM', 'RECHARGE']
    states = []
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
        for b in range(0, 6):
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
            return None



    def pick_random_actions(self):
        rand_index = random.randint(0, len(self.actions)-1)
        return self.actions[rand_index]

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

        v_value = [0] * len(self.states)  # the value at index i is the performance for the state i in states
        # v_value_prime = [0]*len(self.states)
        while True:
            v_value_prime = v_value
            for ind, s in enumerate(self.states):  # warning it's not in the order we thought
                # list with q_value depending on s and a with our model impossible \
                # to have 2 states from one state and one action
                q_s_a = [0]*len(self.actions)

                # for each action
                for ind_a, a in enumerate(self.actions):
                    r_s_a, p_sPrime_knowingSandA, s_prime = sim.simulate(s, a, 'Dynamic Programming')
                    # warning p_sPrime and s_prime = lists
                    # do sum
                    if not p_sPrime_knowingSandA and not s_prime:
                        q_s_a[ind_a] = r_s_a
                    elif len(p_sPrime_knowingSandA) == len(s_prime):
                        q_s_a[ind_a] = r_s_a
                        for i, p in enumerate(p_sPrime_knowingSandA):
                            ind_s_prime = self.find_index_of_new_state(s_prime[i])
                            if ind_s_prime is None:
                                break
                            q_s_a[ind_a] += self.discounted_factor * p * v_value_prime[ind_s_prime]
                        #print(q_s_a)
                # compute max value
                ind_a_max, v_value[ind] = self.max_perf(q_s_a)
                self.policy.add_optimized_policy(s, self.actions[ind_a_max])

            if self.infinite_normal(v_value, v_value_prime) <= self.epsilon:
                break
        print("performance: ", v_value)
        self.policy.show_policy()


if __name__ == "__main__":
    dp = DynamicProgramming()
    dp.main()