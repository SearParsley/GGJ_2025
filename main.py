import curses
import time
from TextBox import Text_Box
from TextPath import Text_Path
import palette

def load_ascii_art(file_path):
  with open(file_path, 'r') as file:
    return file.read()

def draw_ascii_art(ascii_art, start_x, start_y, window, color):
  for i, line in enumerate(ascii_art.splitlines()):
    window.addstr(i + start_y, start_x, line, color)

  # for i, line in enumerate(ascii_bug.splitlines()):
  #   bug_window.addstr(i, 0, line)



def game_loop(stdscr=curses.window):
  curses.curs_set(0)
  stdscr.nodelay(True)
  stdscr.clear()

  # master window
  stdscr = curses.initscr()

  palette.init_colors()

  num_rows, num_cols = stdscr.getmaxyx()
  middle_row = int(num_rows / 2)

  # Text box
  box_height = 10
  box_width = num_cols - 2
  box_y = num_rows - box_height
  box_x = 2
  text_box = Text_Box(box_height, box_width, box_y, box_x)

  # bug!
  bug_x = 16
  bug_y = 4
  bug_color = curses.color_pair(17)
  ascii_bug = load_ascii_art('ASCII/bug.txt')
  bug_window = curses.newwin(num_rows, num_rows, bug_y, bug_x)
  draw_ascii_art(ascii_bug, bug_x, bug_y, bug_window, bug_color)

  def show_bug():
    bug_window.refresh
    
  


  dialogue_tree = [
    ("Welcome to the dialogue tree!", [
      ("Show me the bug", bug_window.refresh),
    ]),
  ]



  text_path = Text_Path(dialogue_tree)


  # Display current text and options
  current_text = text_path.get_current_text()
  options = text_path.get_options()
  text_box.draw_box(current_text, options)

  key_state = None  # Track the current key state
  last_key_time = time.time()  # Timestamp of the last key press
  key_count = 0  # Count of valid key presses
  key_pressed = False  # Flag to track if key is pressed

  while True:
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
          text_box.draw_box(current_text, options)

    # Reset key state if no key is pressed for a short period
    if current_time - last_key_time > 0.2:  # 200ms debounce period
      key_pressed = False

    time.sleep(0.01)  # Small delay to reduce CPU usage



  # center_y = num_rows - box_height
  # mid_height = 20
  # mid_width = 80
  # mid_y = int((num_rows - mid_height - box_height) / 2)
  # mid_x = int((num_cols - mid_width) / 2)
  # center_window = curses.newwin(mid_height, mid_width, mid_y, mid_x)
  # center_window.bkgd('.')


  # center_window.refresh()








  # Initialize color in a separate step


if __name__ == '__main__':    
  curses.wrapper(game_loop)

  