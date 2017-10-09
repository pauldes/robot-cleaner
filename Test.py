import State
import Policy

class Test :
    def test_policy(self,p):
        state = State.State(5, [0, 0], [0, 0], [[1, 1, 1], [1, 1, 1]])
        action = "VACUUM"

        # Adding a rule in the policy
        p.add_optimized_policy(state,action)
        p.show_policy()

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
        if p.state_already_exists(state):
            print("State already exists : Success")
        else:
            print("State already exists : Fail")

        # Find the action
        if p.find_the_action(state) == substitution_action:
            print("Find the action : Success")
        else:
            print("Find the action : Fail")








if __name__ == "__main__":
    p = Policy.Policy()
    test = Test()
    test.test_policy(p)




