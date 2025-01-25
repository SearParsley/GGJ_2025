import curses
import subprocess
import os
from TextBox import Text_Box
from TextPath import Text_Path
import palette

def load_ascii_art(file_path):
  with open(file_path, 'r') as file:
    return file.read()

def draw_ascii_art(ascii_art, start_x, start_y, window=curses.window):
  for i, line in enumerate(ascii_art.splitlines()):
    window.addstr(i + start_x, start_y, line)




def game_loop(stdscr):
  curses.curs_set(0)
  stdscr.clear()

  # master window
  stdscr = curses.initscr()

  palette.init_colors()

  dialogue_tree = {
    "start": (
      "Welcome to the dialogue tree!",
      [("Go to option 1", "option1"), ("Go to option 2", "option2")]
    ),
    "option1": (
      "You chose option 1. What next?",
      [("Return to start", "start"), ("Go to option 2", "option2")]
    ),
    "option2": (
      "You chose option 2. What next?",
      [("Return to start", "start"), ("Go to option 1", "option1")]
    ),
  }



  text_path = Text_Path(dialogue_tree)

  num_rows, num_cols = stdscr.getmaxyx()
  middle_row = int(num_rows / 2)

  # Test box
  box_height = 10
  box_width = num_cols - 2
  box_y = num_rows - box_height
  box_x = 2
  text_box = Text_Box(box_height, box_width, box_y, box_x)

  while True:
    # Display current text and options
    current_text = text_path.get_current_text()
    options = text_path.get_options()
    text_box.draw_box(current_text, options)

    # Wait for user input
    key = stdscr.getch()

    if key == ord('q'):  # Quit the game
      break
    elif key in range(ord('1'), ord('1') + len(options)):
      # Choose the option based on user input
      option_index = key - ord('1')
      text_path.choose_option(option_index)

  


  center_y = num_rows - box_height
  mid_height = 20
  mid_width = 80
  mid_y = int((num_rows - mid_height - box_height) / 2)
  mid_x = int((num_cols - mid_width) / 2)
  center_window = curses.newwin(mid_height, mid_width, mid_y, mid_x)
  center_window.bkgd('.')


  center_window.refresh()


  while True:
    key = box.get_input()
    if key == ord('1'): break
    box.update_text()








  # Initialize color in a separate step

  ascii_bug = load_ascii_art('ASCII/bug.txt')
  bug_window = curses.newwin(4, 12, 0, 0)
  for i, line in enumerate(ascii_bug.splitlines()):
    bug_window.addstr(i, 0, line)

  bug_window.refresh()


  c = stdscr.getch()

  curses.endwin()

  # Convert the key to ASCII and print ordinal value
  print("You pressed %s which is keycode %d." % (chr(c), c))


  curses.napms(3000)












  # Change style: bold, highlighted, and underlined text
  screen.addstr("Regular text\n")
  screen.addstr("Bold\n", curses.A_BOLD)
  screen.addstr("Highlighted\n", curses.A_STANDOUT)
  screen.addstr("Underline\n", curses.A_UNDERLINE)
  screen.addstr("Regular text again\n")

  # Create a custom color set that you might re-use frequently
  # Assign it a number (1-255), a foreground, and background color.
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
  screen.addstr("RED ALERT!\n", curses.color_pair(1))

  # Combine multiple attributes with bitwise OR
  screen.addstr("SUPER RED ALERT!\n", curses.color_pair(1) | curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)

  # Assign it a number (1-255), a foreground, and background color.
  curses.init_pair(64, 64+16, curses.COLOR_BLACK)
  screen.addstr("TEST\n", curses.color_pair(64))

  screen.refresh()
  curses.napms(3000)

  # lines, columns, start line, start column
  my_window = curses.newwin(15, 20, 0, 0)

  # Long strings will wrap to the next line automatically
  # to stay within the window
  my_window.addstr(4, 4, "Hello from 4,4")
  my_window.addstr(5, 15, "Hello from 5,15 with a long string")

  # Print the window to the screen
  my_window.refresh()
  curses.napms(2000)

  # Clear the screen, clearing my_window contents that were printed to screen
  # my_window will retain its contents until my_window.clear() is called.
  screen.clear()
  screen.refresh()

  # Move the window and put it back on screen
  # If we didn't clear the screen before doing this,
  # the original window contents would remain on the screen
  # and we would see the window text twice.
  my_window.mvwin(10, 10)
  my_window.refresh()
  curses.napms(1000)

  # Clear the window and redraw over the current window space
  # This does not require clearing the whole screen, because the window
  # has not moved position.
  my_window.clear()
  my_window.refresh()
  curses.napms(1000)



  # Make a pad 100 lines tall 20 chars wide
  # Make the pad large enough to fit the contents you want
  # You cannot add text larger than the pad
  # We are only going to add one line and barely use any of the space
  pad = curses.newpad(100, 100)
  pad.addstr("This text is thirty characters")

  # Start printing text from (0,2) of the pad (first line, 3rd char)
  # on the screen at position (5,5)
  # with the maximum portion of the pad displayed being 20 chars x 15 lines
  # Since we only have one line, the 15 lines is overkill, but the 20 chars
  # will only show 20 characters before cutting off
  pad.refresh(0, 2, 5, 5, 15, 20)

  curses.napms(3000)

  curses.endwin()


if __name__ == '__main__':    
  curses.wrapper(game_loop)

  