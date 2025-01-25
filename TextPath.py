import curses
class Text_Path:
  """Manages a dialogue tree with branching paths."""
  def __init__(self, dialogue_tree=dict):
    """
    Initialize the Text_Path with a dialogue tree.
    
    :param dialogue_tree: A dictionary representing the dialogue tree.
                          Keys are node IDs, and values are tuples of (text, options).
                          Each option is a tuple of (option_text, next_node_id).
    """
    self.dialogue_tree = dialogue_tree
    self.current_node = "start"  # Start at the root node

  def get_current_text(self):
    """Get the text of the current dialogue node."""
    return self.dialogue_tree[self.current_node][0]

  def get_options(self):
    """Get the options for the current dialogue node."""
    return self.dialogue_tree[self.current_node][1]

  def choose_option(self, option_index):
    """Navigate to the next node based on the selected option."""
    options = self.get_options()
    if 0 <= option_index < len(options):
      self.current_node = options[option_index][1]
    else:
      raise ValueError("Invalid option index")