import Simulator
import Policy
import State
import random
from Simulator import pool_of_actions
import copy

def regroupListBySums(list,size_of_sums):
        shortened_list = []
        shortened_list.append(0)
        counter=0
        n=0
        # Regroup every 2 items of the list
        for perf in list:
            if(counter>size_of_sums):
                counter=0
                n+=1
                shortened_list.append(perf)
            else:
                counter +=1
                shortened_list[n] += perf
        return shortened_list

class MonteCarlo:

    epsilon = 0.1
    gama = 0.9

    def run(self, limit, episode_length):

        list_perf = []
        s0 = State.State(5, [0,0], [0,0], [[1,1,1],[1,1,1]])
        PI_policy = Policy.Policy()
        simulator = Simulator.Simulator()
        # Average reward for a tuple (s,a)
        Q_function = {}
        # Number of times we have met a tuple (s,a)
        SA_counter = {}
        all_states_visited = []
        reward_per_s = {}
        previous_hash = ""
        hash_s2 = ""

        for n in range(0,limit):
            perf = 0

            # First state s0 : everything is dirty
            list_possible_next_states = []
            s0 = State.State(5, [0,0], [0,0], [[1,1,1],[1,1,1]])
            list_possible_next_states.append(s0)

            # Next scenarios of the episode are computed in a loop

            for m in range(0,episode_length):

                s2 = random.choice(list_possible_next_states)
                s2copy = s2.copy()
                previous_hash = hash_s2
                hash_s2 = s2.getHash()

                random_number = random.uniform(0, 1)

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

                # Getting the best action for s2
                r_max2 = -1000
                best_action2 = ""

                #Refresh policy with best action

                if(hash_s2 != previous_hash):
                    for (s,a),r in Q_function.items():
                        if(s == hash_s2):
                            if r > r_max2:
                                r_max2 = r
                                best_action2 = a
                    PI_policy.add_optimized_policy(s2copy, best_action2)

                #print(a2)
                #s2copy.pretty_print()


                #print(r)
                if r2>=100:
                    #print('BEST CASE')
                    break
                elif r2<=(-100):
                    #print('BREAK, WORST CASE')
                    break

            # Getting the performance
            #s2copy.pretty_print()
            #print('ENDED with '+a2)
            list_perf.append(perf)

        return list_perf

if __name__ == "__main__":
  print('testing monte-carlo')
  monte_carlo = MonteCarlo()
  print  (monte_carlo.run(5,10))
  print('done')

