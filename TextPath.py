import curses
class Text_Path:
  """Manages a dialogue tree with branching paths."""
  def __init__(self, dialogue=list):
    """
    Initialize the Text_Path with a dialogue tree.
    """
    self.dialogue = dialogue
    self.current_text = self.dialogue[0][0]
    self.options = self.dialogue[0][1]

  def get_current_text(self):
    """Get the text of the current dialogue node."""
    return self.current_text
  
  def set_dialogue(self, text=str, options=list):
    """
    Set the dialogue for the text path.

    :param options: A list consisting of tuples size 2.
                    Each option is a tuple of (option_text=str, action=function)
    """
    self.current_text = self.dialogue[0][0]
    self.options = self.dialogue[0][1]

  def get_options(self):
    """Get the options for the current dialogue node."""
    return self.options

  def choose_option(self, option_index):
    """Choose a dialogue option and execute the action."""
    _, action = self.options[option_index]
    action()

  def unknown(self):
    self.current_text = "cool"
    self.options = []
