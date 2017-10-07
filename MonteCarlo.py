import Simulator
import Policy
import State

class MonteCarlo:
    epsilon = 0.01
    gama = 0.99

    # Generation of an episode
    s = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
    s.pick_a_random_state()

    p = Policy.Policy()
    a = p.random_policy()

    simulator = Simulator.Simulator()
    r, list_possible_next_states = simulator.simulate(s, a, "Monte-Carlo")