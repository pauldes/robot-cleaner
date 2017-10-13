import Simulator
import Policy
import State
import random
from Simulator import pool_of_actions

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

    epsilon = 0.8
    gama = 0.99

    def run(self, limit, episode_length):

        starting_epsilon = self.epsilon
        list_perf = []
        PI_policy = Policy.Policy()
        simulator = Simulator.Simulator()
        # Number of times we have met a tuple (s,a)
        SA_counter = {}
        all_states_visited = []
        reward_per_s = {}
        previous_hash = ""
        hash_s2 = ""
        reward_max_list=[]
        # Average reward for a tuple (s,a)
        Q_function = {}

        for n in range(0,limit):

            self.epsilon = self.epsilon - (starting_epsilon/limit)
            print('epsilon:'+str(self.epsilon))

            print("Boucle "+str(n)+" sur "+str(limit))
            perf = 0

            # First state s0 : everything is dirty
            list_possible_next_states = []
            s0 = State.State(State.BATTERY_CAPACITY, [0,0], [0,0], [[1,1,1],[1,1,1]])
            hash_s0 = s0.getHash()
            list_possible_next_states.append(s0)

            episode_scenarios = []

            # GENERATE A FULL EPISODE
            for m in range(0,episode_length):

                # Choosing a state
                current_state = random.choice(list_possible_next_states)

                # Choosing an action
                random_number = random.uniform(0, 1)
                if random_number > self.epsilon :
                    if (PI_policy.state_already_exists(current_state.getHash())):
                        current_action = PI_policy.find_the_action(current_state)
                    else:
                        current_action = random.choice(pool_of_actions)
                else:
                    current_action = random.choice(pool_of_actions)

                # Simulate reward
                current_reward, list_possible_next_states = simulator.simulate(current_state.copy(), current_action, "Monte-Carlo")

                # Add state, action, reward in the episode
                episode_scenarios.append([current_state.copy(), current_action, current_reward])



            # COMPUTE DATA

            encountered_sa = []

            for m in range(0,episode_length):


                s_hash = episode_scenarios[m][0].getHash()
                action = episode_scenarios[m][1]
                #print('m = '+str(m))



                if [s_hash,action] not in encountered_sa:
                    encountered_sa.append([s_hash,action])
                    sum_rewards = 0
                    for n in range(m,episode_length):
                        sum_rewards += episode_scenarios[n][2] * self.gama**(n-m)

                    if(s_hash,action) in SA_counter:
                        Q_function[s_hash,action] = (sum_rewards + (SA_counter[s_hash,action])*Q_function[s_hash,action]) / (SA_counter[s_hash,action]+1.0)
                        SA_counter[s_hash,action] += 1
                    else:
                        SA_counter[s_hash,action] = 1
                        Q_function[s_hash,action] = sum_rewards+0.0

            for scenario in episode_scenarios:
                reward_max = -1000
                best_action = ""
                for (s_hash,a),r in Q_function.items():
                    if(s_hash == scenario[0].getHash()):
                        if r > reward_max:
                            reward_max = r
                            best_action = a
                PI_policy.add_optimized_policy(scenario[0].copy(), best_action)

            perf = -1000
            for (s_hash,a),r in Q_function.items():
                if(s_hash == hash_s0):
                    if r > perf:
                        perf = r
            list_perf.append(perf)

        return list_perf
        print(list_perf)

if __name__ == "__main__":
  print('testing monte-carlo')
  monte_carlo = MonteCarlo()
  print  (monte_carlo.run(100,10))
  print('done')

