import random

ROOM_SIZE_X = 3
ROOM_SIZE_Y = 2
BATTERY_CAPACITY = 5

class State:

    #class variable shared  by all instances
    sizeX = ROOM_SIZE_X #colonne
    sizeY = ROOM_SIZE_Y #line
    battery_capacity = BATTERY_CAPACITY

    def __init__(self, battery, posRobot, posBase, roomGrid):
        #initialisation through the passed state
        self.battery = battery
        self.posRobot = posRobot
        self.posBase = posBase
        self.roomGrid = roomGrid


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
        #print("battery level : ", self.battery, ", posRobot : ", self.posRobot, ", posBase", self.posBase)
        for l, line in enumerate(self.roomGrid):
            for e, elem in enumerate(line):
                self.roomGrid[l][e] = random.randint(0, 1)
        #print(self.roomGrid)
        #self.pretty_print()



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

    def getHash(self):
        full = []
        for x in range(0,self.sizeX):
          for y in range(0,self.sizeY):
            full.append( self.roomGrid[y][x] )
        full.append(self.battery)
        full.append(self.posRobot[0])
        full.append(self.posRobot[1])
        full.append(self.posBase[0])
        full.append(self.posBase[1])
        full.append(self.battery)
        full_text =""
        for c in full:
          full_text+=str(c)
        return full_text

