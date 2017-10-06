
import State
import random

#########################################

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
reward_cell_clean =    {action_vacuum : -5,  action_recharge : 0,   action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : 0}
reward_cell_dirty =    {action_vacuum : 5,   action_recharge : 0,   action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : 0}
reward_battery_empty = {action_vacuum : -20, action_recharge : 10,  action_move_left : -20, action_move_right : -20, action_move_up : -20, action_move_down : -20}
reward_battery_full =  {action_vacuum : -1,  action_recharge : -10, action_move_left : -1,  action_move_right : -1,  action_move_up : -1,  action_move_down : -1}
reward_battery_inter = {action_vacuum : -1,  action_recharge : 0,   action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : 0 }
reward_wall_left =     {action_vacuum : 0,  action_recharge : 0, action_move_left : -10, action_move_right : 0,  action_move_up : 0,  action_move_down : 0}
reward_wall_right =    {action_vacuum : 0,  action_recharge : 0, action_move_left : 0,  action_move_right : -10, action_move_up : 0,  action_move_down : 0}
reward_wall_top =      {action_vacuum : 0,  action_recharge : 0, action_move_left : 0,  action_move_right : 0,  action_move_up : -10, action_move_down : 0}
reward_wall_bottom =   {action_vacuum : 0,  action_recharge : 0, action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : -10}


# Walls surrounding the robot
def wallLeft(s):
  return s.posRobot[0]==0
def wallRight(s):
  return s.posRobot[0]==State.ROOM_SIZE_X-1
def wallTop(s):
  return s.posRobot[1]==0
def wallBottom(s):
  return s.posRobot[1]==State.ROOM_SIZE_Y-1
def currentCellIsDirty(s):
  return 1==s.roomGrid[s.posRobot[1]][s.posRobot[0]]
def batteryFull(s):
  return s.battery==State.BATTERY_CAPACITY
def batteryEmpty(s):
  return s.battery==0

class Simulator:


  def simulate(self,state,action,algorithm):

    # The simulator receive a state and an action

    print('Algorithm: '+algorithm)
    print('I received the state')
    state.prettyPrint()
    print('and the action '+action)

    # He computes the reward

    reward = 0

    # Wall configuration
    if(wallLeft(s)):
      #print("There is a Wall on the left")
      reward += reward_wall_left[action]
    if(wallRight(s)):
      #print("There is a Wall on the right")
      reward += reward_wall_right[action]
    if(wallTop(s)):
      #print("There is a Wall on the top")
      reward += reward_wall_top[action]
    if(wallBottom(s)):
      #print("There is a Wall on the bottom")
      reward += reward_wall_bottom[action]

    # Battery configuration
    if(batteryEmpty(s)):
      #print("The battery is empty")
      reward += reward_battery_empty[action]
    if(batteryFull(s)):
      #print("The battery is full")
      reward += reward_battery_full[action]
    if((batteryFull(s) or batteryEmpty(s))==False):
      #print('The battery is intermediate')
      reward += reward_battery_inter[action]

    # Current cell configuration
    if(currentCellIsDirty(s)):
      #print('The current cell is dirty as fuck')
      reward += reward_cell_dirty[action]
    else:
      #print('The current cell is clean')
      reward += reward_cell_clean[action]


    print('The reward is '+str(reward))

    # s' = s.doAction(a) ...


    if(algorithm==algo_DP):
      print()
      # Will return P(s'|s,a) pour tous s' possibles, et s', and R(s,a)
      # Forme : r,[Ps'1 , Ps'2, ...],[s'1, s'2]
      return reward
    if(algorithm==algo_TD or algorithm==algo_MC):
      print()
      # s.doAction(a) ...
      # Will return R(s,a) and all possible s'

#########################################


simulator = Simulator()
s = State.State()
a = random.choice(pool_of_actions)
simulator.simulate(s,a,algo_DP)




