import curses

'''
dialogue: text=str, [
  (option1=str, action=function, requirement=str/None),
  (option2=str, action=function, requirement=str/None),
  (option3=str, action=function, requirement=str/None),
])
'''

class Text_Path:
  """Manages a dialogue tree with branching paths."""
  def __init__(self, dialogue=tuple):
    """
    Initialize the Text_Path with a dialogue tree.
    """
    self.dialogue = dialogue
    self.current_text = dialogue[0]
    self.options = dialogue[1]

  def get_current_text(self):
    """Get the text of the current dialogue node."""
    return self.current_text

  def set_current_text(self, new_current_text):
    """Set the text of the current dialogue node."""
    self.current_text = new_current_text

  def get_options(self):
    """Get the available options for the current dialogue node."""
    available_options = []
    for option in self.options:
      option_text = option[0]
      action = option[1]
      requirement = option[2]
      if requirement is None or requirement:
        available_options.append((option_text, action))
    return available_options

  def set_options(self, new_options):
    """Set the text of the current dialogue node."""
    self.options = new_options

  def choose_option(self, option_index):
    """Choose a dialogue option and execute the action."""
    action = self.options[option_index][1]
    action()
