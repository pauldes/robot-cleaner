import Simulator
import Policy
import State
import random

class MonteCarlo:

    epsilon = 0.01
    gama = 0.99

    def run(self, limit):

        n=0
        s1 = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
        p = Policy.Policy()
        simulator = Simulator.Simulator()

        # Average reward for a tuple (s,a)
        Q_function = {}
        # Number of times we have met a tuple (s,a)
        SA_counter = {}

        while(n<limit):

            n+=1
            G = {}

            # We choose randomly s1
            s1.pick_a_random_state()
            a1 = p.random_policy()
            r1, list_possible_next_states = simulator.simulate(s1, a1, "Monte-Carlo")

            G[s1.getHash(),a1] = r1
            if(s1.getHash(),a1) in SA_counter:
                Q_function[s1.getHash(),a1] = (r1 + (SA_counter[s1.getHash(),a1])*Q_function[s1.getHash(),a1]) / (SA_counter[s1.getHash(),a1]+1.0)
                SA_counter[s1.getHash(),a1] += 1
            else:
                SA_counter[s1.getHash(),a1] = 1
                Q_function[s1.getHash(),a1] = r1 +0.0


            # We choose randomly s2 within the possible new states
            s2 = random.choice(list_possible_next_states)
            a2 = p.random_policy()
            r2, list_possible_next_states = simulator.simulate(s2, a2, "Monte-Carlo")

            G[s2.getHash(),a2] = r2
            if(s2.getHash(),a2) in SA_counter:
                Q_function[s2.getHash(),a2] = (r2 + (SA_counter[s2.getHash(),a2])*Q_function[s2.getHash(),a2]) / (SA_counter[s2.getHash(),a2]+1.0)
                SA_counter[s2.getHash(),a2] += 1
            else:
                SA_counter[s2.getHash(),a2] = 1
                Q_function[s2.getHash(),a2] = r2 +0.0

            # We choose randomly s3 within the possible new states
            s3 = random.choice(list_possible_next_states)
            a3 = p.random_policy()
            r3, list_possible_next_states = simulator.simulate(s3, a3, "Monte-Carlo")

            G[s3.getHash(),a3] = r3
            if(s3.getHash(),a3) in SA_counter:
                Q_function[s3.getHash(),a3] = (r3 + (SA_counter[s3.getHash(),a3])*Q_function[s3.getHash(),a3]) / (SA_counter[s3.getHash(),a3]+1.0)
                SA_counter[s3.getHash(),a3] += 1
            else:
                SA_counter[s3.getHash(),a3] = 1
                Q_function[s3.getHash(),a3] = r3 +0.0

            #print(G)

            #TODO foreach s appearing in the episode do π ← greedy w.r.t Q0 end

        #print(Q_function)
        #print(SA_counter)

if __name__ == "__main__":
  print('testing monte-carlo')
  monte_carlo = MonteCarlo()
  monte_carlo.run(100)
  print('done')
