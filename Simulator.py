
import State

#########################################

def robotIsOnBase(s):
  return s.posRobot==s.posBase

def wallUp(s):
  return True

def wallDown(s):
  return True

def wallRight(s):
  return True

def wallLeft(s):
  return True

#########################################

class Simulator:
  def launch():
    hey = 'hey'
    a = State
    print(wallUp(a))

#########################################

s = Simulator
s.launch()



