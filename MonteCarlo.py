import Simulator
import Policy
import State
import random
from Simulator import pool_of_actions
import copy

class MonteCarlo:

    epsilon = 0.01
    gama = 0.99

    def run(self, limit):

        n=0
        list_perf = []
        s1 = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
        PI_policy = Policy.Policy()
        simulator = Simulator.Simulator()

        # Average reward for a tuple (s,a)
        Q_function = {}
        # Number of times we have met a tuple (s,a)
        SA_counter = {}
        all_states_visited = []
        reward_per_s = {}

        while(n<limit):

            n+=1
            perf = 0
            random_number = random.uniform(0, 1)
            G = {}

            # LENGTH-3 EPISODES
            # #TODO more length

            # We choose randomly s1
            #s1.pick_a_random_state()
            #
            #NOW we choose always the same s1
            s1 = State.State(5, [0,0], [0,0], [[1,1,1],[1,1,1]])
            s1copy = copy.deepcopy(s1)
            hash_s1 = s1.getHash()
            if random_number > self.epsilon :
                if(PI_policy.state_already_exists(s1.getHash())):
                    a1 = PI_policy.find_the_action(s1)
                else:
                    a1 = random.choice(pool_of_actions)
            else:
                a1 = random.choice(pool_of_actions)

            r1, list_possible_next_states = simulator.simulate(s1, a1, "Monte-Carlo")

            perf = perf + r1


            if(hash_s1,a1) in SA_counter: #Have already seen this action before
                Q_function[hash_s1,a1] = (r1 + (SA_counter[hash_s1,a1])*Q_function[hash_s1,a1]) / (SA_counter[hash_s1,a1]+1.0)
                SA_counter[hash_s1,a1] += 1
            else: #First time we see this action
                SA_counter[hash_s1,a1] = 1
                Q_function[hash_s1,a1] = r1 +0.0


            # We choose randomly s2 within the possible new states
            s2 = random.choice(list_possible_next_states)
            s2copy = copy.deepcopy(s2)
            hash_s2 = s2.getHash()
            if random_number > self.epsilon :
                if (PI_policy.state_already_exists(s2.getHash())):
                    a2 = PI_policy.find_the_action(s2)
                else:
                    a2 = random.choice(pool_of_actions)
            else:
                a2 = random.choice(pool_of_actions)
            r2, list_possible_next_states = simulator.simulate(s2, a2, "Monte-Carlo")
            perf = perf + r2

            if(hash_s2,a2) in SA_counter:
                Q_function[hash_s2,a2] = (r2 + (SA_counter[hash_s2,a2])*Q_function[hash_s2,a2]) / (SA_counter[hash_s2,a2]+1.0)
                SA_counter[hash_s2,a2] += 1
            else:
                SA_counter[hash_s2,a2] = 1
                Q_function[hash_s2,a2] = r2 +0.0



            # We choose randomly s3 within the possible new states
            s3 = random.choice(list_possible_next_states)
            s3copy = copy.deepcopy(s3)
            hash_s3 = s3.getHash()
            if random_number > self.epsilon:
                if (PI_policy.state_already_exists(s3.getHash())):
                    a3 = PI_policy.find_the_action(s3)
                else:
                    a3 = random.choice(pool_of_actions)
            else:
                a3 = random.choice(pool_of_actions)
            r3, list_possible_next_states = simulator.simulate(s3, a3, "Monte-Carlo")
            perf = perf + r3

            if(hash_s3,a3) in SA_counter:
                Q_function[hash_s3,a3] = (r3 + (SA_counter[hash_s3,a3])*Q_function[hash_s3,a3]) / (SA_counter[hash_s3,a3]+1.0)
                SA_counter[hash_s3,a3] += 1
            else:
                SA_counter[hash_s3,a3] = 1
                Q_function[hash_s3,a3] = r3 +0.0



            #print(G)

            # Getting the performance
            list_perf.append(perf)


            #Getting the best action for s1
            r_max = -1000
            best_action = ""

            for (s,a),r in Q_function.items():
                if(s == hash_s1):
                    if r > r_max:
                        r_max = r
                        best_action = a
            #print(best_action)
            PI_policy.add_optimized_policy(s1copy, best_action)


            # Getting the best action for s2
            r_max2 = -1000
            best_action2 = ""

            if(hash_s2 != hash_s1):
                for (s,a),r in Q_function.items():
                    if(s == hash_s2):
                        if r > r_max2:
                            r_max2 = r
                            best_action2 = a
                #print(best_action2)
                PI_policy.add_optimized_policy(s2copy, best_action2)



            # Getting the best action for s3
            r_max3 = -1000
            best_action3 = ""

            if (hash_s3 != hash_s2 and hash_s3 != hash_s1):
                for (s,a),r in Q_function.items():
                    if(s == hash_s3):
                        if r > r_max3:
                            r_max3 = r
                            best_action3 = a
                #print(best_action3)
                PI_policy.add_optimized_policy(s3copy, best_action3)





            #PI_policy.show_policy()

                #slide 136

            #print('Q-function built with '+str(len(Q_function))+ ' different tuples (s,a)')
            #print(Q_function)
            #
        #print(list_perf)

        shortened_list_perf = []
        shortened_list_perf.append(0)
        MAX_COUNTER=10
        counter=0
        n=0
        # Regroup every 100 items of the list
        for perf in list_perf:
            if(counter>MAX_COUNTER):
                counter=0
                n+=1
                shortened_list_perf.append(perf)
            else:
                counter +=1
                shortened_list_perf[n] += perf

        print(shortened_list_perf)


if __name__ == "__main__":
  print('testing monte-carlo')
  monte_carlo = MonteCarlo()
  monte_carlo.run(10000)
  print('done')
