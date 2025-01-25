import curses
import time
from TextBox import Text_Box
from TextPath import Text_Path
from TextImage import Text_Image
from GameState import Game_State
import palette

game_state = Game_State()

def observe(text_path=Text_Path):
  """Action for observing surroundings"""
  if game_state.get_health() <= 50:
    # leaves fall out
    text_path.set_current_text("") # TODO: low health dialogue
    text_path.set_options([
      ("", exit, None),
      ("", exit, None),
    ])
  elif game_state.has_item("Flower"):
    # attract an animal
    text_path.set_current_text("") # TODO: flower dialogue
    text_path.set_options([
      ("", exit, None),
      ("", exit, None),
    ])
  elif game_state.has_item("Bark"):
    # woodpecker
    text_path.set_current_text("") # TODO: bark dialogue
    text_path.set_options([
      ("", exit, None),
      ("", exit, None),
    ])

def grow(text_path=Text_Path):
  """Action for growth"""
  if game_state.get_health() <= 50:
    # leaves fall out
    text_path.set_current_text("") # TODO: low health dialogue
    text_path.set_options([
      ("", exit, None),
      ("", exit, None),
    ])
  elif game_state.has_item("Moss"):
    # heal some health
    text_path.set_current_text("") # TODO: flower dialogue
    text_path.set_options([
      ("", exit, None),
      ("", exit, None),
    ])
  elif game_state.has_item("Bark"):
    # woodpecker
    text_path.set_current_text("") # TODO: bark dialogue
    text_path.set_options([
      ("", exit, None),
      ("", exit, None),
    ])

def player_death(text_path=Text_Path, text_box=Text_Box):
  current_text = "No further actions are available. Whether it be age or decay, your life has met its end. Game Over."
  options = [("Exit Game", exit, None)]
  text_path.set_current_text(current_text)
  text_path.set_options(options)
  new_options = text_path.get_options()
  text_box.draw_box(current_text, new_options)




def game_loop(stdscr=curses.window):

  # set up
  curses.curs_set(0)
  stdscr.nodelay(True)
  stdscr.clear()
  stdscr = curses.initscr()
  palette.init_colors()




  '''
  Title Screen
  '''
  
  num_rows, num_cols = stdscr.getmaxyx()
  middle_row = int(num_rows / 2)
  middle_column = int(num_cols / 2)

  title = Text_Image('ASCII/temp.txt', stdscr, curses.color_pair(16))
  title_x = middle_column - int(title.get_width() / 2) + 4
  title_y = middle_row - int(title.get_height() * 1) + 2

  instructions_text = "Press any button to start"
  instructions_x = middle_column - int(len(instructions_text) / 2) - 2
  instructions_y = middle_row + 4

  ascii_bug = Text_Image('ASCII/bug.txt', stdscr, curses.color_pair(17))
  bug_x = 76
  bug_y = 15

  # draw title stuff
  title.draw(title_x, title_y)
  stdscr.addstr(instructions_y, instructions_x, instructions_text, curses.color_pair(16) | curses.A_BLINK)
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

  dialogue_tree = (
    f"Standing at a modest height of {game_state.get_height()}, ",
    [
      ("Observe your suroundings", observe, None),
      ("Attend to growth", grow, None),
    ],
  )

  text_path = Text_Path(dialogue_tree)

  # Display current text and options
  current_text = text_path.get_current_text()
  options = text_path.get_options()
  text_box.draw_box(current_text, options)

  key_state = None  # Track the current key state
  last_key_time = time.time()  # Timestamp of the last key press
  key_count = 0  # Count of valid key presses
  key_pressed = False  # Flag to track if key is pressed








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
          player_death(text_path, text_box)

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

  