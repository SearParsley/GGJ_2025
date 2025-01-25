import curses

class Text_Image:
  def __init__(self, path, window, color):
    self.path = path
    self.window = window
    self.color = color

    with open(self.path, 'r') as file:
      self.text = file.read()
    
  def draw(self, start_x, start_y):
    for i, line in enumerate(self.text.splitlines()):
      self.window.addstr(i + start_y, start_x, line, self.color)

  def show(self):
    self.window.refresh()
