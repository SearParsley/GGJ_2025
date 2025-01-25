import curses


colors = [
  180, # light brown
  240, # light gray
]

def init_colors():
  curses.start_color()

  for i in range(len(colors)):
    print(colors[i])
    curses.init_pair(i+16, colors[i], curses.COLOR_BLACK)
