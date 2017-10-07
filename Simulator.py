

import random
import State

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


# Apply an action to a state and get the possible next states with associate probabilities
def compute_next_states(state,action):

  next_possible_states = []
  next_state = state

  # Battery
  if(action == action_recharge and batteryFull(state)==False):
      next_state.battery = state.battery+1
  if(action == action_recharge and batteryFull(state)):
      next_state.battery = state.battery
  if(action != action_recharge and state.battery > 0):
      next_state.battery = state.battery-1

  # Position
  if(action == action_move_left and wallLeft(state)==False):
      next_state.posRobot[0] = state.posRobot[0] - 1

  if(action == action_move_right and wallRight(state)==False):
      next_state.posRobot[0] = state.posRobot[0] + 1

  if(action == action_move_up and wallTop(state)==False):
      next_state.posRobot[1] = state.posRobot[1] - 1

  if(action == action_move_down and wallBottom(state)==False):
      next_state.posRobot[1] = state.posRobot[1] + 1


   # Current Cell
  if(action==action_vacuum and currentCellIsDirty(state)) :
     #TODO, temporary to avoid 2 possible s' (still dirty 0.33 and clean 0.66)
     next_state.roomGrid[state.posRobot[1]][state.posRobot[0]]=0

  elif(action==action_vacuum and currentCellIsDirty(state)==False) :
     next_state.roomGrid[state.posRobot[1]][state.posRobot[0]]=0
     #so.. nothing happens

  next_possible_states.append([next_state,1])
  #Only 1 for now

  #For testing:
  return next_possible_states

# Compute the reward for a State s and an action
def compute_reward(s,action):
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
  return reward


class Simulator:


  def simulate(self,state,action,algorithm):

    # The simulator receives a state and an action

    print('Algorithm: '+algorithm)
    print('I received the state')
    state.prettyPrint()
    print('and the action '+action)

    reward = compute_reward(state,action)
    print('The reward is '+str(reward))

    next_possible_states = compute_next_states(state,action)
    print('The next possible states are: ')

    list_of_next_possible_states=[]
    list_of_next_possible_probabilities=[]

    for state,probability in next_possible_states:
      state.prettyPrint()
      print("with probability p="+str(probability))
      list_of_next_possible_states.append(state)
      list_of_next_possible_probabilities.append(probability)


    if(algorithm==algo_DP):
      # Will return P(s'|s,a) pour tous s' possibles, et s', and R(s,a)
      # Forme : r,[Ps'1 , Ps'2, ...],[s'1, s'2]
      return reward, list_of_next_possible_probabilities, list_of_next_possible_states

    if(algorithm==algo_TD or algorithm==algo_MC):
      # Will return R(s,a) and all possible s'
      return reward, list_of_next_possible_states

#########################################

if __name__ == "__main__":
  simulator = Simulator()
  s = State.State()
  a = random.choice(pool_of_actions)
  simulator.simulate(s,a,algo_DP)

