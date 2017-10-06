import random

class State:

    #class variable shared  by all instances
    # Setting the room size
    sizeX = 2 #colonne
    sizeY = 2 #line

    def __init__(self, battery, posRobot, posBase, roomGrid):
        if battery and posRobot and posBase and roomGrid:
            #initialisation through the passed state
            self.battery = battery
            self.posRobot = posRobot
            self.posBase = posBase
            self.roomGrid = roomGrid
        else :
            #initial arbitrary state
            # Picking some values for the robot and base initial position
            self.battery = 5  # Battery life. Between 0 & 5.
            self.posRobot = self.random_tuple()  # (x,y)
            self.posBase = self.random_tuple()  # (x,y)
            self.roomGrid = [[1] * self.sizeX] * self.sizeY  # 0=clean, 1=dirty. #roomGrid[ligne][colonne]

    def randrange_float(self, start, stop, step): # allow to choose a random value between start and stop with a step
        return random.randint(0, int((stop - start) / step)) * step + start

    def random_tuple(self):
        rand_int_x = random.randint(0, self.sizeX - 1)
        rand_int_y = random.randint(0, self.sizeY - 1)
        return [rand_int_x, rand_int_y]

    def is_the_same(self, other_state):
        return self.battery == other_state.battery and self.posBase == other_state.posBase \
               and self.posRobot == other_state.posRobot and self.roomGrid == other_state.roomGrid

    def pick_a_random_state(self):
        #self.battery = self.randrange_float(0, 5, 0.5)
        self.battery = random.randint(0, 5)
        self.posRobot = self.random_tuple()
        self.posBase = self.random_tuple()
        print("battery level : ", self.battery, ", posRobot : ", self.posRobot, ", posBase", self.posBase)
        for l, line in enumerate(self.roomGrid):
            for e, elem in enumerate(line):
                self.roomGrid[l][e] = random.randint(0, 1)
        print(self.roomGrid)
        self.pretty_print()



    #Pretty-printing the state
    def pretty_print(self):
        # Note: only for 3*2 matrix (for now...)
        matrix  = [[' ',' ',' '],[' ',' ',' ']]
        matrix[self.posRobot[1]][self.posRobot[0]] = 'r'
        matrix[self.posBase[1]][self.posBase[0]] = 'b'
        matrix2 = [[' ' if i==0 else 'x' for i in self.roomGrid[0]],[' ' if i==0 else 'x' for i in self.roomGrid[1]]]
        print('----- STATE -----')
        print('    -|'+self.battery*'o'+ (5-self.battery)*'' + '|+' )
        print('     Room:')
        print('     |'+matrix2[0][0]+'|'+matrix2[0][1]+'|'+matrix2[0][2]+'|')
        print('     |'+matrix2[1][0]+'|'+matrix2[1][1]+'|'+matrix2[1][2]+'|')
        print('     Robot:')
        print('     |'+matrix[0][0]+'|'+matrix[0][1]+'|'+matrix[0][2]+'|')
        print('     |'+matrix[1][0]+'|'+matrix[1][1]+'|'+matrix[1][2]+'|')

    def __str__(self):
        return "State: battery "+ str(self.battery)+ " robot "+ str(self.posRobot) +" base "+ str(self.posBase)+ " room "+ str(self.roomGrid)