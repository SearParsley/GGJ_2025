import curses

class Text_Image:
  def __init__(self, path:str, window:curses.window, color:int):
    self.path = path
    self.window = window
    self.color = color
    self.width = 0
    self.height = 0

    with open(self.path, 'r') as file:
      text = file.read()
      self.text = text
      for line in self.text.splitlines():
        self.height += 1
        self.width = max(len(line), self.width)


  def draw(self, start_x:int, start_y:int):
    for i, line in enumerate(self.text.splitlines()):
      self.window.addstr(i + start_y, start_x, line, self.color)

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height

  
