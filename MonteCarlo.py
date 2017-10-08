import Simulator
import Policy
import State
import random
from Simulator import pool_of_actions

class MonteCarlo:

    epsilon = 0.01
    gama = 0.99



    def run(self, limit):

        n=0
        s1 = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
        PI_policy = Policy.Policy()
        simulator = Simulator.Simulator()

        # Average reward for a tuple (s,a)
        Q_function = {}
        # Number of times we have met a tuple (s,a)
        SA_counter = {}
        all_states_visited = []
        reward_per_s = {}

        #while(n<limit):

        #n+=1
        G = {}

        # LENGTH-3 EPISODES

        # We choose randomly s1
        s1.pick_a_random_state()
        hash_s1 = s1.getHash()
        a1 = random.choice(pool_of_actions)

        r1, list_possible_next_states = simulator.simulate(s1, a1, "Monte-Carlo")


        if(hash_s1,a1) in SA_counter: #Have already seen this action before
            Q_function[hash_s1,a1] = (r1 + (SA_counter[hash_s1,a1])*Q_function[hash_s1,a1]) / (SA_counter[hash_s1,a1]+1.0)
            SA_counter[hash_s1,a1] += 1
        else: #First time we see this action
            SA_counter[hash_s1,a1] = 1
            Q_function[hash_s1,a1] = r1 +0.0

        # We choose randomly s2 within the possible new states
        s2 = random.choice(list_possible_next_states)
        hash_s2 = s2.getHash()
        a2 = random.choice(pool_of_actions)
        r2, list_possible_next_states = simulator.simulate(s2, a2, "Monte-Carlo")

        if(hash_s2,a2) in SA_counter:
            Q_function[hash_s2,a2] = (r2 + (SA_counter[hash_s2,a2])*Q_function[hash_s2,a2]) / (SA_counter[hash_s2,a2]+1.0)
            SA_counter[hash_s2,a2] += 1
        else:
            SA_counter[hash_s2,a2] = 1
            Q_function[hash_s2,a2] = r2 +0.0

        # We choose randomly s3 within the possible new states
        s3 = random.choice(list_possible_next_states)
        hash_s3 = s3.getHash()
        a3 = random.choice(pool_of_actions)
        r3, list_possible_next_states = simulator.simulate(s3, a3, "Monte-Carlo")

        if(hash_s3,a3) in SA_counter:
            Q_function[hash_s3,a3] = (r3 + (SA_counter[hash_s3,a3])*Q_function[hash_s3,a3]) / (SA_counter[hash_s3,a3]+1.0)
            SA_counter[hash_s3,a3] += 1
        else:
            SA_counter[hash_s3,a3] = 1
            Q_function[hash_s3,a3] = r3 +0.0

        #print(G)


        #TODO
        r_max = -1000
        best_action = ""

        for (s,a),r in Q_function.items():
            if(s == hash_s1):
                if r > r_max:
                    r_max = r
                    best_action = a
        print(best_action)


        r_max2 = -1000
        best_action2 = ""

        if(hash_s2 != hash_s1):
            for (s,a),r in Q_function.items():
                if(s == hash_s2):
                    if r > r_max2:
                        r_max2 = r
                        best_action2 = a
            print(best_action2)

        r_max3 = -1000
        best_action3 = ""

        if (hash_s3 != hash_s2):
            for (s,a),r in Q_function.items():
                if(s == hash_s3):
                    if r > r_max3:
                        r_max3 = r
                        best_action3 = a
            print(best_action3)


            #slide 136

        print('Q-function built with '+str(len(Q_function))+ ' different tuples (s,a)')
        print(Q_function)
        #print(SA_counter)

if __name__ == "__main__":
  print('testing monte-carlo')
  monte_carlo = MonteCarlo()
  monte_carlo.run(1000)
  print('done')
