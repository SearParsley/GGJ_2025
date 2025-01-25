import curses

class Game_State:
  def __init__(self, window:curses.window):
    self.window = window
    self.health = 100
    self.luck = 0
    self.resources = [
      "Bark", "Leaves", "Grubs"
    ]
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

  def add_resource(self, resource:str):
    """Add a resource to the player."""
    self.resources.append(resource)

  def remove_resource(self, resource:str):
    """Remove a resource from the player."""
    if resource in self.resources:
      self.resources.remove(resource)

  def has_resource(self, resource:str):
    """Check if the player has access to a specific resource."""
    return True
    return resource in self.resources






