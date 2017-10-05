import random
from State import State
from Simulator import Simulator
import Policy



class DynamicProgramming:
    #actions dictionnary
    actions = ['MOVE_LEFT', 'MOVE_RIGHT', 'MOVE_UP', 'MOVE_DOWN', 'VACUUM', 'RECHARGE', 'MOVE']
    states = []
    mode = 1

    epsilon = 0.01
    discounted_factor = 0.99
    #policy = Policy()

    def generate_all_states(self):
        roomG = [[0] * State.sizeX] * State.sizeY

        for b in range(0,6):
            for prx in range(0, State.sizeX-1):
                for pry in range(0, State.sizeY-1):
                    for pbx in range(0, State.sizeX-1):
                        for pby in range(0, State.sizeY-1):
                            for i in range(0, 2):
                                for rgl in range(0, State.sizeX - 1):
                                    for rgc in range(0, State.sizeY-1):
                                        roomG[rgl][rgc] = i
                                #here the room is finished
                                # print(roomG)
                                ns = State(b,[prx,pry],[pbx,pby],roomG)
                                print(b,[prx,pry],[pbx,pby],roomG)
                                if ns not in self.states:
                                    self.states.append(ns)


    def pick_random_actions(self):
        rand_index = random.randint(0, len(self.actions)-1)
        return self.actions[rand_index]

    def main(self):
        sim = Simulator()
        self.generate_all_states()
        print(len(self.states))
        v_value = [0] * len(self.states)
        v_value_prime =[0]*len(self.states)
       # while True:



        #sim.launch()


if __name__=="__main__":
    dp=DynamicProgramming()
    dp.main()