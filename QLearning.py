import random
from State import State
from Simulator import Simulator
from Simulator import pool_of_actions, robotOnBase, roomClean, batteryEmpty
from Policy import Policy


class QLearning:
    # actions dictionnary
    initial_state = State(State.battery_capacity, [0, 0], [0, 0], [[1] * State.sizeX] * State.sizeY )
    mode = 3

    epsilon = 0.01
    alpha = 0.1
    discounted_factor = 0.99
    policy = Policy()

    def choose_probabilistic_action(self, best_action, q_all_actions):
        A = len(pool_of_actions)
        p_best = 1.0 - self.epsilon + (self.epsilon/A)
        other_p = self.epsilon/A
        # create a list of cumulative probabilities depending on the best_action
        cum_prob = [0.0] * A
        sum = 0.0
        rand = random.random()
        # print('rand', rand, 'p_best', p_best, 'other_p', other_p, 'best action ', best_action)
        for i, p in enumerate(cum_prob):
            if i == pool_of_actions.index(best_action):
                sum += p_best
                p = sum
            else:
                sum += other_p
                p = sum
            if rand <= sum:
                return pool_of_actions[i], q_all_actions[i]
                break



    def main(self):
        self.policy.init_arbitrary_policy(self.initial_state)
        sim = Simulator()

        for l in range(0, 1):
            s = self.initial_state
            while True:
                # action choose randomly depending on the distribution and best_action for the state and this policy
                a_best, q_s = self.policy.epsilone_greedy(s)

                a, q_s_a = self.choose_probabilistic_action(a_best, q_s)
                #print('before', s.getHash(), 'action', a)
                r_s_a, s_prime = sim.simulate(s.copy(), a, 'Temporal Differences')
                a_prime_best, q_s_prime = self.policy.epsilone_greedy(s_prime[0])
                a_prime, q_s_prima_a_prime = self.choose_probabilistic_action(a_prime_best, q_s_prime)
                delta = r_s_a + self.discounted_factor*q_s_prima_a_prime - q_s_a
                # update value q_s_a
                q_s_a += self.alpha*delta
                self.policy.update_optimized_policy(s, a, q_s_a)
                #print('state', s.getHash(),  ' q_s_a ', q_s_a)
                s = s_prime[0].copy()
                if (robotOnBase(s) and roomClean(s)) or roomClean(s) or (batteryEmpty(s) and not roomClean(s) and not robotOnBase(s)):
                    print('final state :', s.getHash())
                    break
            print('performance qlearning :', self.policy.get_performance(self.initial_state))

if __name__ == "__main__":
    ql = QLearning()
    ql.main()