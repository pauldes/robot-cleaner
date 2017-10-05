
import State

#########################################

# Robot is at the charging base
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
# Current cell
def currentCellIsDirty(s):
  return 1==s.roomGrid[s.posRobot[1]][s.posRobot[0]]

# Actions
action_move_left = 'MOVE_LEFT'
action_move_right = 'MOVE_RIGHT'
action_move_up = 'MOVE_UP'
action_move_down = 'MOVE_DOWN'
action_vacuum = "VACUUM"
action_recharge = "RECHARGE"
action_move = "MOVE?" #TODO will disappear

# Rewards
reward_battery_empty = {action_vacuum : -20, action_move : -20, action_recharge : 10}
reward_battery_full =  {action_vacuum : -1,  action_move : -1,  action_recharge : -10}
reward_cell_clean =    {action_vacuum : -1,  action_move : -1,  action_recharge : 0}
reward_cell_dirty =    {action_vacuum : 5,   action_move : -1,  action_recharge : 0}
reward_battery_empty = {action_vacuum : -20, action_move : -20, action_recharge : 10}
reward_battery_full =  {action_vacuum : -1,  action_move : -1,  action_recharge : -10}
reward_battery_inter = {action_vacuum : -1,  action_move : -1,  action_recharge : 0}
#TODO replace action_move with 4 directions
reward_wall_left = {action_vacuum : -1, action_recharge : -1}
reward_wall_right = {action_vacuum : -1, action_recharge : -1}
reward_wall_top = {action_vacuum : -1, action_recharge : -1}
reward_wall_bottom = {action_vacuum : -1, action_recharge : -1}
#TODO add reward for 4 directions

#########################################

class Simulator:
    def launch(self, state, action, mode):
      #mode 1=DP , 2=MC, 3=QL
        self.state = State(state)
        self.state.pretty_print()
        self.mode = mode
        self.action = action
        self.reward = 0
        self.proba=0







