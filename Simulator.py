import random
from State import State


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
reward_cell_clean =    {action_vacuum : -10,  action_recharge : 0,   action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : 0}
reward_cell_dirty =    {action_vacuum : 30,   action_recharge : 0,   action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : 0}
reward_battery_empty = {action_vacuum : -20, action_recharge : 10,  action_move_left : -20, action_move_right : -20, action_move_up : -20, action_move_down : -20}
reward_battery_full =  {action_vacuum : -1,  action_recharge : -10, action_move_left : -1,  action_move_right : -1,  action_move_up : -1,  action_move_down : -1}
reward_battery_inter = {action_vacuum : -1,  action_recharge : 5,   action_move_left : -1,  action_move_right : -1,  action_move_up : -1,  action_move_down : -1 }
reward_wall_left =     {action_vacuum : 0,  action_recharge : 0, action_move_left : -10, action_move_right : 0,  action_move_up : 0,  action_move_down : 0}
reward_wall_right =    {action_vacuum : 0,  action_recharge : 0, action_move_left : 0,  action_move_right : -10, action_move_up : 0,  action_move_down : 0}
reward_wall_top =      {action_vacuum : 0,  action_recharge : 0, action_move_left : 0,  action_move_right : 0,  action_move_up : -10, action_move_down : 0}
reward_wall_bottom =   {action_vacuum : 0,  action_recharge : 0, action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : -10}
reward_robot_off_base= {action_vacuum : 0,  action_recharge : -20, action_move_left : 0,  action_move_right : 0,  action_move_up : 0,  action_move_down : 0}

# Walls surrounding the robot
def wallLeft(s):
    return s.posRobot[0] == 0

def wallRight(s):
    return s.posRobot[0] == State.sizeX-1

def wallTop(s):
    return s.posRobot[1] == 0

def wallBottom(s):
    return s.posRobot[1] == State.sizeY-1

def currentCellIsDirty(s):
    return 1 == s.roomGrid[s.posRobot[1]][s.posRobot[0]]

def batteryFull(s):
    return s.battery == State.battery_capacity

def batteryEmpty(s):
    return s.battery == 0

def robotOnBase(s):
  return s.posRobot[0] == s.posBase[0] and s.posRobot[1] == s.posBase[1]

def roomClean(s):
  for ligne in s.roomGrid:
    for case in ligne:
      if(case==1):
        return False
  return True

# Apply an action to a state and get the possible next states with associate probabilities
def compute_next_states(state, action):

    next_possible_states = []
    next_state = state.copy()

    # Battery
    if action == action_recharge and not batteryFull(state) and robotOnBase(state):
        next_state.battery = state.battery + 1
    elif action == action_recharge and batteryFull(state) and robotOnBase(state):
        next_state.battery = state.battery
    elif action != action_recharge and state.battery > 0:
        next_state.battery = state.battery - 1


    # Position
    if action == action_move_left and not wallLeft(state) and state.battery > 0:
        next_state.posRobot[0] = state.posRobot[0] - 1

    if action == action_move_right and not wallRight(state) and state.battery > 0 :
        # print(str(next_state), str(state))
        next_state.posRobot[0] = state.posRobot[0] + 1
        # print(str(next_state), str(state))

    if action == action_move_up and not wallTop(state) and state.battery > 0 :
        next_state.posRobot[1] = state.posRobot[1] - 1

    if action == action_move_down and not wallBottom(state) and state.battery > 0:
        next_state.posRobot[1] = state.posRobot[1] + 1

    # Current Cell
    if action == action_vacuum and currentCellIsDirty(state) and state.battery > 0:
        # TODO, temporary to avoid 2 possible s' (still dirty 0.33 and clean 0.66)
        next_state.roomGrid[state.posRobot[1]][state.posRobot[0]] = 0

    elif action == action_vacuum and not currentCellIsDirty(state) and state.battery > 0 :
        next_state.roomGrid[state.posRobot[1]][state.posRobot[0]] = 0
        # so.. nothing happens

    next_possible_states.append([next_state, 1])

    # Only 1 for now

    #  testing:
    return next_possible_states


# Compute the reward for a State s and an action
def compute_reward(s, action):
    reward = 0

    # Wall configuration
    if wallLeft(s):
        reward += reward_wall_left[action]
    if wallRight(s):
        reward += reward_wall_right[action]
    if wallTop(s):
        reward += reward_wall_top[action]
    if wallBottom(s):
        reward += reward_wall_bottom[action]
    # Battery configuration
    if batteryEmpty(s):
        reward += reward_battery_empty[action]
    if batteryFull(s):
        reward += reward_battery_full[action]
    if not (batteryFull(s) or batteryEmpty(s)):
        reward += reward_battery_inter[action]
    # Current cell configuration
    if currentCellIsDirty(s):
        reward += reward_cell_dirty[action]
    else:
        reward += reward_cell_clean[action]

    #Ending points

    if(robotOnBase(s) and roomClean(s)):
      reward += 200
    elif(roomClean(s)):
      reward += 100
    elif(batteryEmpty(s) and roomClean(s)==False and robotOnBase(s)==False):
      reward += -200

    # Charging off base
    if not robotOnBase(s):
        reward += reward_robot_off_base[action]
    return reward


    # The simulator receives a state and an action

class Simulator:
    def simulate(self,state,action,algorithm):

        # The simulator receives a state and an action

        # print('Algorithm: '+algorithm)
        # print('I received the state')
        # state.pretty_print()
        # print('and the action '+action)

        reward = compute_reward(state, action)
        # print('The reward is '+str(reward))


        next_possible_states = compute_next_states(state, action)
        # print('The next possible states are: ')

        list_of_next_possible_states = []
        list_of_next_possible_probabilities = []

        for state, probability in next_possible_states:
            # state.pretty_print()
            # print("with probability p="+str(probability))
            list_of_next_possible_states.append(state)
            list_of_next_possible_probabilities.append(probability)


        if algorithm == algo_DP:
            # Will return P(s'|s,a) pour tous s' possibles, et s', and R(s,a)
            # Forme : r,[Ps'1 , Ps'2, ...],[s'1, s'2]
            return reward, list_of_next_possible_probabilities, list_of_next_possible_states

        if algorithm == algo_TD or algorithm == algo_MC:
            # Will return R(s,a) and all possible s'
            return reward, list_of_next_possible_states
#########################################
