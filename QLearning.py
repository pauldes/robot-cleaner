import random
from State import State
from Simulator import Simulator
from Simulator import pool_of_actions
from Policy import Policy


class QLearning:
    # actions dictionnary
    initial_state = State(State.battery_capacity, [0, 0], [0, 0], [[1] * State.sizeX] * State.sizeY )
    mode = 3

    epsilon = 0.01
    alpha = 0.1
    discounted_factor = 0.99
    policy = Policy()

    def choose_probabilitic_action(self, best_action):
        A = len(pool_of_actions)
        p_best = 1.0 - self.epsilon + (self.epsilon/A)
        other_p = self.epsilon/A
        # create a list of cumulative probabilities depending on the best_action
        cum_prob = [0.0] * A
        sum = 0.0
        rand = random.random()
        for i, p in enumerate(cum_prob):
            if i == pool_of_actions.index(best_action):
                sum += p_best
                p = sum
            else:
                sum += other_p
                p = sum
            if rand <= sum :
                return pool_of_actions[i]
                break



    def main(self):
        self.policy.init_arbitrary_policy(self.initial_state)
        sim = Simulator()

        while True:
            s = self.initial_state
            while True:
                # action choose randomly depending on the distribution and best_action for the state and this policy
                a, q_s_a = self.choose_probabilitic_action(self.policy.epsilone_greedy(s))
                r_s_a, s_prime = sim.simulate(s, a, 'Temporal Differences')
                a_prime, q_s_prima_a_prime = self.choose_probabilitic_action(self.policy.epsilone_greedy(s_prime))
                delta = r_s_a + self.discounted_factor*q_s_prima_a_prime - q_s_a
                # update value q_s_a
                q_s_a += self.alpha*delta
                self.policy.update_optimized_policy(s, a, q_s_a)
                s = s_prime




if __name__ == "__main__":
    ql = QLearning()
    ql.main()