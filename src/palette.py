import curses


colors = [
  180, # light brown : 16 : text box
  250, # light gray  : 17 : bug color
  240, # dark gray   : 18 : 
  136, # dark yellow : 19 : beehive
  28,  # dark green  : 20 : tree
  166, # orange      : 21 : fire
  131, # dark brown  : 22 : bark
  220, # med yellow  : 23 : sun
  25,  # dark blue   : 24 : rain
]

def init_colors():
  curses.start_color()

  for i, color in enumerate(colors):
    print(color)
    curses.init_pair(i+16, color, curses.COLOR_BLACK)
