
import State
import random

#########################################

# Robot is at the charging base - IS IT USEFUL ?
def robotIsAtBase(s):
  return s.posRobot==s.posBase
# Walls surrounding the robot
def wallLeft(s):
  return s.posRobot[0]==0
def wallRight(s):
  return s.posRobot[0]==s.sizeX-1
def wallTop(s):
  return s.posRobot[1]==0
def wallBottom(s):
  return s.posRobot[1]==s.sizeY-1
def currentCellIsDirty(s):
  return 1==s.roomGrid[s.posRobot[1]][s.posRobot[0]]
def batteryFull(s):
  return s.battery==State.BATTERY_CAPACITY

#Algorithms
algo_MC = 'Monte-Carlo'
algo_TD = 'Temporal Differences'
algo_DP = 'Dynamic Programming'

# Actions
action_move_left = 'MOVE_LEFT'
action_move_right = 'MOVE_RIGHT'
action_move_up = 'MOVE_UP'
action_move_down = 'MOVE_DOWN'
action_vacuum = "VACUUM"
action_recharge = "RECHARGE"
pool_of_actions = [action_move_left,action_move_right,action_move_up,action_move_down,action_vacuum,action_recharge]

# Rewards
reward_cell_clean =    {action_vacuum : -1,  action_recharge : 0,   action_move_left : -1,  action_move_right : -1,  action_move_up : -1,  action_move_down : -1}
reward_cell_dirty =    {action_vacuum : 5,   action_recharge : 0,   action_move_left : -1,  action_move_right : -1,  action_move_up : -1,  action_move_down : -1}
reward_battery_empty = {action_vacuum : -20, action_recharge : 10,  action_move_left : -20, action_move_right : -20, action_move_up : -20, action_move_down : -20}
reward_battery_full =  {action_vacuum : -1,  action_recharge : -10, action_move_left : -1,  action_move_right : -1,  action_move_up : -1,  action_move_down : -1}
reward_battery_inter = {action_vacuum : -1,  action_recharge : 0,   action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : 0 }
reward_wall_left =     {action_vacuum : -1,  action_recharge : -1, action_move_left : -10, action_move_right : -1,  action_move_up : -1,  action_move_down : -1}
reward_wall_right =    {action_vacuum : -1,  action_recharge : -1, action_move_left : -1,  action_move_right : -10, action_move_up : -1,  action_move_down : -1}
reward_wall_top =      {action_vacuum : -1,  action_recharge : -1, action_move_left : -1,  action_move_right : -1,  action_move_up : -10, action_move_down : -1}
reward_wall_bottom =   {action_vacuum : -1,  action_recharge : -1, action_move_left : -1,  action_move_right : -1,  action_move_up : -1,  action_move_down : -10}


#########################################

class Simulator:

  def simulate(self,state,action,algorithm):

    if(algorithm==algo_DP):
      print()
      ##
    if(algorithm==algo_TD):
      print()
      ##
    if(algorithm==algo_DP):
      print()
      ##

    print('I received the state')
    state.prettyPrint()
    print('and the action '+action)




    print('The reward is '+)

    # TODO Apply the action a to the State s
    #  s.doAction(a) ...




#########################################

simulator = Simulator()
s = State.State()
a = random.choice(pool_of_actions)
simulator.simulate(s,a)




