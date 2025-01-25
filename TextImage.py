import curses

class Text_Image:
  def __init__(self, path, window, color):
    self.path = path
    self.window = window
    self.color = color
    self.width = 0
    self.height = 0

    with open(self.path, 'r') as file:
      self.text = file.read()

    # for line in enumerate(self.text.splitlines()):
    #   self.height += 1
    #   if len(line) > self.width: self.width = len(line)
    
  def draw(self, start_x, start_y):
    for i, line in enumerate(self.text.splitlines()):
      self.window.addstr(i + start_y, start_x, line, self.color)

  def refresh(self):
    self.window.refresh()

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height

  
