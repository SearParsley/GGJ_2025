import curses
import time
import random
from TextBox import Text_Box
from TextPath import Text_Path
from TextImage import Text_Image
from GameState import Game_State
import palette



def get_lucky(game_state):
  """Get a lucky integer between 0 to 100"""
  return min(random.randrange(70) + (random.random() * game_state.get_luck()), 100)


def fire(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def lumberjack(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def storm(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def woodpecker(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def snow(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def uneventful(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def bird(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def rain(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def friend(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def sun(game_state):
  text_path.set_current_text("text prompt")
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])


def pass_time(game_state):
  """Action for passing time surroundings"""
  chance = get_lucky(game_state)

  if    chance <= 10: fire(game_state)
  elif  chance <= 20: lumberjack(game_state)
  elif  chance <= 30: storm(game_state)
  elif  chance <= 40: woodpecker(game_state)
  elif  chance <= 50: snow(game_state)
  elif  chance <= 60: uneventful(game_state)
  elif  chance <= 70: bird(game_state)
  elif  chance <= 80: rain(game_state)
  elif  chance <= 90: friend(game_state)
  elif chance <= 100: sun(game_state)



def grow(game_state):
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
  


initial_dialogue = (
  "You are a lone tree. Winter is approaching. Do what you must to survive.",
  [
    ("Stand tall against the sands of time", pass_time, None),
    # ("Attend to growth", grow, None),
  ],
)

text_path = Text_Path(initial_dialogue)



def game_loop(stdscr=curses.window):

  # set up
  curses.curs_set(0)
  stdscr.nodelay(True)
  stdscr = curses.initscr()
  stdscr.clear()
  palette.init_colors()

  game_state = Game_State(stdscr)

  '''
  Title Screen
  '''
  
  num_rows, num_cols = stdscr.getmaxyx()
  middle_row = int(num_rows / 2)
  middle_column = int(num_cols / 2)

  title = Text_Image('./ASCII/title.txt', stdscr, curses.color_pair(16)) # TODO: title text color
  title_x = middle_column - int(title.get_width() / 2) + 4
  title_y = middle_row - int(title.get_height() * 1) + 2

  instructions_text = "Press any button to start"
  instructions_x = middle_column - int(len(instructions_text) / 2) - 2
  instructions_y = middle_row + 4

  ascii_bug = Text_Image('./ASCII/bug.txt', stdscr, curses.color_pair(17)) # TODO: bug color
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
          text_path.choose_option(option_index, game_state)

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

  