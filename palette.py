import curses


colors = [
  180, # light brown : 16
  250, #  light gray : 17
  240, #   dark gray : 18
]

def init_colors():
  curses.start_color()

  for i in range(len(colors)):
    print(colors[i])
    curses.init_pair(i+16, colors[i], curses.COLOR_BLACK)
