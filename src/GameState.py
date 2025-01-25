import curses

class Game_State:
  def __init__(self, window:curses.window):
    self.window = window
    self.health = 100
    self.luck = 0
    self.resources = []
    self.num_rows, self.num_cols = window.getmaxyx()


  def get_window(self):
    return self.window

  def set_window(self, new_window:curses.window):
    self.window = new_window

  def get_health(self):
    return self.health

  def set_health(self, new_health:int):
    self.health = new_health

  def get_luck(self):
    return self.luck

  def set_luck(self, new_luck:int):
    self.luck = min(new_luck, 30)

  def add_item(self, item:str):
    """Add an item to the player's resources."""
    self.resources.append(item)

  def remove_item(self, item:str):
    """Remove an item from the player's resources."""
    if item in self.resources:
      self.resources.remove(item)

  def has_item(self, item:str):
    """Check if the player's resources contains a specific item."""
    return item in self.resources






'''
resources:
moss - heal over time
fruit - offering to others
flowers - attract others
bark - reduce damage taken
nest - birds




'''