import curses
import time
import random
from TextBox import Text_Box
from TextPath import Text_Path
from TextImage import Text_Image
from GameState import Game_State
import palette



game_state = Game_State()




def get_lucky():
  """Get a lucky integer between 0 to 100"""
  return random.randrange(70) + game_state.get_luck()



def pass_time():
  """Action for passing time surroundings"""
  chance = get_lucky()

  if chance <= 10:
    # lumberjack
    text_path.set_current_text("lumberjack") # TODO: lumberjack dialogue
    text_path.set_options([
      ("lumberjack", pass_time, None),
      ("lumberjack", pass_time, None),
    ])
  elif chance <= 20:
    # mushrooms start growing
    text_path.set_current_text("mushrooms") # TODO: mushrooms dialogue
    text_path.set_options([
      ("mushrooms", pass_time, None),
      ("mushrooms", pass_time, None),
    ])
  elif chance <= 30:
    # attract a woodpecker
    text_path.set_current_text("woodpecker") # TODO: woodpecker dialogue
    text_path.set_options([
      ("woodpecker", pass_time, "Sap"),
      ("woodpecker", pass_time, None),
    ])
  elif chance <= 40:
    # nothing eventful happens
    text_path.set_current_text("friend") # TODO: nothing dialogue
    text_path.set_options([
      ("Take time to photosynthesize", pass_time, "Flower"),
      ("friend", pass_time, None),
    ])
  elif chance <= 50:
    # x
    text_path.set_current_text("friend") # TODO: x dialogue
    text_path.set_options([
      ("friend", pass_time, "Flower"),
      ("friend", pass_time, None),
    ])
  elif chance <= 60:
    # attract a friend
    text_path.set_current_text("x") # TODO: friend dialogue
    text_path.set_options([
      ("x", pass_time, "Flower"),
      ("x", pass_time, None),
    ])
  elif chance <= 70:
    # x
    text_path.set_current_text("x") # TODO: x dialogue
    text_path.set_options([
      ("x", pass_time, "Flower"),
      ("x", pass_time, None),
    ])
  elif chance <= 80:
    # x
    text_path.set_current_text("x") # TODO: x dialogue
    text_path.set_options([
      ("x", pass_time, "Flower"),
      ("x", pass_time, None),
    ])
  else:
    # bountiful rain
    text_path.set_current_text("rain") # TODO: rain dialogue
    text_path.set_options([
      ("rain", pass_time, None),
      ("rain", pass_time, None),
    ])



def grow():
  """Action for growth"""
  text_path.set_current_text("testing")
  text_path.set_options([
    ("pass time", pass_time, None),
    ("grow again", grow, None),
  ])



def player_death(text_path, text_box):
  current_text = "No further actions are available. By age or decay, your life has met its end. Game Over."
  options = [("Exit Game", exit, None)]
  text_path.set_current_text(current_text)
  text_path.set_options(options)
  new_options = text_path.get_options()
  text_box.draw_box(current_text, new_options)
  


dialogue_tree = (
  f"Standing at a modest height of {game_state.get_height()}, ",
  [
    ("Observe your suroundings", observe, None),
    ("Attend to growth", grow, None),
  ],
)

text_path = Text_Path(dialogue_tree)



def game_loop(stdscr=curses.window):

  # set up
  curses.curs_set(0)
  stdscr.nodelay(True)
  stdscr = curses.initscr()
  stdscr.clear()
  palette.init_colors()



  '''
  Title Screen
  '''
  
  num_rows, num_cols = stdscr.getmaxyx()
  middle_row = int(num_rows / 2)
  middle_column = int(num_cols / 2)

  title = Text_Image('ASCII/title.txt', stdscr, curses.color_pair(16)) # TODO: title text color
  title_x = middle_column - int(title.get_width() / 2) + 4
  title_y = middle_row - int(title.get_height() * 1) + 2

  instructions_text = "Press any button to start"
  instructions_x = middle_column - int(len(instructions_text) / 2) - 2
  instructions_y = middle_row + 4

  ascii_bug = Text_Image('ASCII/bug.txt', stdscr, curses.color_pair(17)) # TODO: bug color
  bug_x = 76
  bug_y = 15

  # draw title stuff
  title.draw(title_x, title_y)
  stdscr.addstr(instructions_y, instructions_x, instructions_text, curses.color_pair(16) | curses.A_BLINK) # TODO: instructions text color
  ascii_bug.draw(bug_x, bug_y)

  stdscr.refresh()
  

  while True:
    # wait for input
    key = stdscr.getch()
    if key != -1: break

    time.sleep(0.01)  # Small delay to reduce CPU usage









  stdscr.clear()
  stdscr.refresh()




  '''
  Main Stuff
  '''

  # Text box
  box_height = 10
  box_width = num_cols - 2
  box_y = num_rows - box_height
  box_x = 2
  text_box = Text_Box(box_height, box_width, box_y, box_x)

  # Display current text and options
  current_text = text_path.get_current_text()
  options = text_path.get_options()
  text_box.draw_box(current_text, options)

  key_state = None  # Track the current key state
  last_key_time = time.time()  # Timestamp of the last key press
  key_count = 0  # Count of valid key presses
  key_pressed = False  # Flag to track if key is pressed






  '''
  Dialogue loop
  '''

  in_dialogue = True

  while in_dialogue:
    key = stdscr.getch()  # Get the key (non-blocking)

    current_time = time.time()

    if key != -1:  # A key is pressed
      if not key_pressed:  # Only process the key if not already pressed
        key_state = key  # Update the key state
        key_pressed = True  # Mark the key as pressed
        last_key_time = current_time  # Reset the timestamp
        key_count += 1

        # Handle specific key presses
        if key_state == ord('q'):  # Quit the game
          break

        elif key_state in range(ord('1'), ord('1') + len(options)):
          # Choose the option based on user input
          option_index = key_state - ord('1')
          text_path.choose_option(option_index)

          # Update current text and options
          current_text = text_path.get_current_text()
          options = text_path.get_options()

          # Draw text box with current text and available options
          text_box.draw_box(current_text, options)

          if len(text_path.get_options()) == 0: in_dialogue = False

    # Reset key state if no key is pressed for a short period
    if current_time - last_key_time > 0.2:  # 200ms debounce period
      key_pressed = False

    time.sleep(0.01)  # Small delay to reduce CPU usage



if __name__ == '__main__':    
  curses.wrapper(game_loop)

  