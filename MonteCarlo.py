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

    # We choose randomly s2 in the possible new states
    s2 = random.choice(list_possible_next_states)

    a2 = p.random_policy()

    r2, list_possible_next_states = simulator.simulate(s2, a2, "Monte-Carlo")

    s3 = random.choice(list_possible_next_states)

    a3 = p.random_policy()

    r3, list_possible_next_states = simulator.simulate(s3, a3, "Monte-Carlo")