import curses
from TextPath import Text_Path

class Text_Box:
  def __init__(self, height:int, width:int, start_y:int, start_x:int):
    self.height = height  # Height of the box
    self.width = width  # Width of the box
    self.start_y = start_y  # Starting y position (row)
    self.start_x = start_x  # Starting x position (column)

    self.window = curses.newwin(height, width, start_y, start_x)

  def wrap_text(self, text:str):
    """Wrap the text to fit within the box width."""
    if not isinstance(text, str): text = str(text)

    wrapped_lines = []
    max_line_length = self.width - 2  # Subtract 2 for the box borders

    while len(text) > max_line_length:
      wrapped_lines.append(text[:max_line_length])
      text = text[max_line_length:]

    # Add any remaining text (it will fit within the box)
    wrapped_lines.append(text)
    return wrapped_lines

  def draw_box(self, text_path:Text_Path):
    """Draw the box and display the text with options."""
    text = text_path.current_text
    options = text_path.get_options()

    self.window.clear()
    self.window.attron(curses.color_pair(16))
    self.window.box()
    self.window.attroff(curses.color_pair(16))

    if not isinstance(text, str): text = str(text)

    # Wrap and display the main text
    wrapped_text = self.wrap_text(text)
    for i, line in enumerate(wrapped_text[:self.height - 3]):  # Reserve space for options
      # Ensure the cursor stays within window bounds
      if 1 + i < self.height - 1:  # Leave 1 space at the bottom for borders
        self.window.addstr(1 + i, 2, line[:self.width - 2])

    # Display the options below the main text
    for i, (option_text, _) in enumerate(options[:self.height - len(wrapped_text) - 2]):
      # Ensure options fit below the text and within the window
      if len(wrapped_text) + 1 + i < self.height - 1:
        option_line = f"{i + 1}. {option_text}"
        self.window.addstr(len(wrapped_text) + 2 + i, 2, option_line[:self.width - 2])

    self.window.refresh()

  def hide_box(self):
    self.window.clear()
