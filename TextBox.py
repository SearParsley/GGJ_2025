class Text_Box:
  def __init__(self, window, width, height, start_y, start_x):
    self.window = window  # Window object to draw the text box
    self.width = width  # Width of the box
    self.height = height  # Height of the box
    self.start_y = start_y  # Starting y position (row)
    self.start_x = start_x  # Starting x position (column)
    self.text = "Press any key to change state!"  # Initial text
    self.text_state_1 = "Press any key to change state!"  # State 1 text
    self.text_state_2 = "You pressed a key!"  # State 2 text

    self.create_box()  # Draw the box initially

  def wrap_text(self, text):
    """Wrap the text to fit within the box width."""
    wrapped_lines = []
    max_line_length = self.width - 2  # Subtract 2 for the box borders

    while len(text) > max_line_length:
      wrapped_lines.append(text[:max_line_length])
      text = text[max_line_length:]

    # Add any remaining text (it will fit within the box)
    wrapped_lines.append(text)
    return wrapped_lines

  def create_box(self):
    """Draw the box and initialize the text inside it."""
    self.window.clear()  # Clear the window before drawing
    self.window.box()  # Draw the border of the box

    wrapped_text = self.wrap_text(self.text)  # Wrap the text
    for i, line in enumerate(wrapped_text):
      # Add each line of wrapped text inside the box
      self.window.addstr(self.start_y + 1 + i, self.start_x + 1, line[:self.width - 2])  # Ensure text doesn't exceed box width

    self.window.refresh()  # Refresh to update the screen

  def update_text(self):
    """Toggle the text between two states."""
    if self.text == self.text_state_1:
      self.text = self.text_state_2
    else:
      self.text = self.text_state_1
    self.create_box()  # Redraw the box with the updated text

  def get_input(self):
    """Wait for a key press and return the key."""
    return self.window.getch()
