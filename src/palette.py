import curses


colors = [
  180, # light brown : 16
  250, #  light gray : 17
  240, #   dark gray : 18
  136, # dark yellow : 19
  28,  #  dark green : 20
]

def init_colors():
  curses.start_color()

  for i, color in enumerate(colors):
    print(color)
    curses.init_pair(i+16, color, curses.COLOR_BLACK)
