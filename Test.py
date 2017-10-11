import State
import Policy
import Simulator

class Test :
    def test_policy(self):
        p = Policy.Policy()
        state = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
        action = "VACUUM"

        # Adding a rule in the policy
        p.add_optimized_policy(state,action)

        test_list = []
        test_list.append([state.getHash(),action])

        if (p.mappingList == test_list):
            print("Adding a rule in the policy : Success")
        else :
            print("Adding a rule in the policy : Fail")

        substitution_action = "MOVE_LEFT"
        p.add_optimized_policy(state,substitution_action)

        test_list.pop()
        test_list.append([state.getHash(),substitution_action])

        if (p.mappingList == test_list):
            print("Changing a rule in the policy : Success")
        else :
            print("Changing a rule in the policy : Fail")

        # State already exist
        if p.state_already_exists(state.getHash()):
            print("State already exists : Success")
        else:
            print("State already exists : Fail")

        # Find the action
        if p.find_the_action(state) == substitution_action:
            print("Find the action : Success")
        else:
            print("Find the action : Fail")

    def test_simulator(self):
        state = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
        action = "VACUUM"
        simulator = Simulator.Simulator()

        # Test next computing states - first test
        battery = state.battery
        posX = state.posRobot[0]
        posY = state.posRobot[1]
        reward, next_state = simulator.simulate(state, action, "Monte-Carlo")

        if(next_state[0].battery == battery - 1):
            print("Next computing states - Battery : Success")
        else:
            print("Next computing states - Battery : Fail")

        if(next_state[0].posRobot[0] == posX and next_state[0].posRobot[1] == posY):
            print("Next computing states - Position : Success")
        else:
            print("Next computing states - Position : Fail")

        if(Simulator.currentCellIsDirty(next_state[0])):
            print("Next computing states - CurrentCell : Fail")
        else:
            print("Next computing states - CurrentCell : Success")

        state = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
        action = "MOVE_RIGHT"

        posX = state.posRobot[0]
        posY = state.posRobot[1]

        reward, next_state = simulator.simulate(state, action, "Monte-Carlo")

        if(next_state[0].battery == battery - 1):
            print("Next computing states 2 - Battery  : Success")
        else:
            print("Next computing states 2 - Battery : Fail")




        if(Simulator.currentCellIsDirty(next_state[0])):
            print("Next computing states 2 - CurrentCell : Success")
        else:
            print("Next computing states 2 - CurrentCell : Fail")

        if(next_state[0].posRobot[0] == posX and next_state[0].posRobot[1] == posY):
            print("Next computing states 2 - Position : Fail ")
        else:
            print("Next computing states 2 - Position : Success")







if __name__ == "__main__" :
    test = Test()
    test.test_policy()
    test.test_simulator()




