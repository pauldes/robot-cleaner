import random

class State:

  battery  = 5              # Battery life. Between 0 & 5.
  posRobot = [random.randint(0,2),random.randint(0,1)]          # x,y
  posBase  = [posRobot[0],posRobot[1]]          # x,y
  roomGrid = [[0, 0, 0],    # 0=clean, 1=dirty.
              [0, 0, 0]]

  def prettyPrint(self):

    matrix  = [[' ',' ',' '],[' ',' ',' ']]
    matrix[self.posRobot[1]][self.posRobot[0]] = 'r'
    matrix[self.posBase[1]][self.posBase[0]] = 'b'

    print ('----- STATE -----')
    print('    -|'+self.battery*'o'+ (5-self.battery)*'' + '|+' )
    print('      Room:')
    print('     | | | |')
    print('     | | | |')
    print('      Robot:')
    print('     |'+matrix[0][0]+'|'+matrix[0][1]+'|'+matrix[0][2]+'|')
    print('     |'+matrix[1][0]+'|'+matrix[1][1]+'|'+matrix[1][2]+'|')
