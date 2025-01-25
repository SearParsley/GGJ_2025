import curses
import subprocess
import os



def load_ascii_art(file_path):
  with open(file_path, 'r') as file:
    return file.read()

def draw_ascii_art(ascii_art, x, y, window=curses.window):
  for i, line in enumerate(ascii_art.splitlines()):
    window.addstr(i + x, y, line)

def main(main_screen):
  # The `screen` is a window that acts as the master window
  # that takes up the whole screen. Other windows created
  # later will get painted on to the `screen` window.
  screen = curses.initscr()

  curses.curs_set(0)

  # Initialize color in a separate step
  curses.start_color()

  ascii_bug = load_ascii_art('ASCII/bug.txt')
  bug_window = curses.newwin(4, 12, 0, 0)
  for i, line in enumerate(ascii_bug.splitlines()):
    bug_window.addstr(i, 0, line)

  bug_window.refresh()
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
  curses.wrapper(main)

  