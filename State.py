import random

ROOM_SIZE_X = 3
ROOM_SIZE_Y = 2
BATTERY_CAPACITY = 5

class State:

  # Picking some values for the robot and base initial position
  randIntX = random.randint(0,ROOM_SIZE_X-1)
  randIntY = random.randint(0,ROOM_SIZE_Y-1)
  # The components of a State:
  battery  = BATTERY_CAPACITY                # Battery life. Between 0 & 5.
  posRobot = [randIntX,randIntY]             # (x,y)
  posBase  = [randIntX,randIntY]             # (x,y)
  roomGrid = [ [0]*ROOM_SIZE_X ]*ROOM_SIZE_Y # 0=clean, 1=dirty.

  # Pretty-printing the state
  def prettyPrint(self):
    # Note: only for 3*2 matrix
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
