import curses
import time
import random
from TextBox import Text_Box
from TextPath import Text_Path
from TextImage import Text_Image
from GameState import Game_State
import palette



def exit_game(game_state:Game_State):
  """Clean up curses and exit the game."""
  curses.endwin()  # Clean up curses
  exit()       # Exit the program




def get_lucky(game_state:Game_State):
  """Get a lucky integer between 0 to 100"""
  return min(random.randrange(50) + (random.random() * game_state.get_luck()), 100)



def bg_center(text_image:Text_Image, game_state:Game_State):
  image_x = int(game_state.num_cols / 2 - text_image.get_width() / 2)
  image_y = int(game_state.num_rows - text_image.get_height() - 11)
  return image_x, image_y



def fire(game_state:Game_State):
  game_state.window.clear()

  ascii_fire = Text_Image('./ASCII/fire.txt', game_state.window, curses.color_pair(21))
  fire_x, fire_y = bg_center(ascii_fire, game_state)
  ascii_fire.draw(fire_x, fire_y)
  game_state.window.refresh()

  text_path.set_current_text("A blazing flame tears through the nearby brush, and it begins to leap towards you.")
  text_path.set_options([
    ("Succumb to the inferno", burn, None),
    ("Prevent major damage by releasing extra hydration", sacrifice_hydration, game_state.has_resource("Hydration")),
    ("Protect yourself with your hardened barkskin", sacrifice_bark, game_state.has_resource("Bark")),
  ])

def sacrifice_bark(game_state:Game_State):
  game_state.remove_resource("Bark")
  game_state.set_luck(game_state.get_luck() + 10)
  text_path.set_current_text("The fire burns through your sturdy bark, reducing it to ash, but the rest of you remains intact.")
  text_path.set_options([
    ("Continue with determination", pass_time, None),
  ])

def sacrifice_hydration(game_state:Game_State):
  game_state.remove_resource("Hydration")
  text_path.set_current_text("The fire steams against your damp bark. You're not as hydrated, but nothing seems to have been damaged.")
  text_path.set_options([
    ("Do some photosynthesizing", pass_time, None),
  ])

def burn(game_state:Game_State):
  for res in ["Acorn", "Moss", "Bark", "Nest"]:
    game_state.remove_resource(res)
  
  game_state.set_health(game_state.get_health() - 50)

  text_path.set_current_text("The fire has harmed you gravely. All flammable resources have been burned away.")
  text_path.set_options([
    ("Do nothing", pass_time, None),
    ("Recover what energy you can", recover, None),
  ])

def lumberjack(game_state:Game_State):
  text_path.set_current_text("lumberjack prompt") # TODO: lumberjack
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def storm(game_state:Game_State):
  text_path.set_current_text("storm prompt") # TODO: storm
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def woodpecker(game_state:Game_State):
  text_path.set_current_text("woodpecker prompt") # TODO: woodpecker
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def snow(game_state:Game_State):
  text_path.set_current_text("snow prompt") # TODO: snow
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def spider(game_state:Game_State):
  text_path.set_current_text("spider prompt") # TODO: spider
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def bird(game_state:Game_State):
  text_path.set_current_text("bird prompt") # TODO: bird
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def rain(game_state:Game_State):
  text_path.set_current_text("rain prompt") # TODO: rain
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def friend(game_state:Game_State):
  text_path.set_current_text("friend prompt") # TODO: friend
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])

def sun(game_state:Game_State):
  text_path.set_current_text("sun prompt") # TODO: sun
  text_path.set_options([
    ("option 1", pass_time, None),
    ("option 2", pass_time, None),
  ])



def check_life(game_state:Game_State):
  if game_state.get_health() <= 0: death(game_state)





# List of (luck threshold, function, cooldown) tuples
events = [
  (10, fire, 3),
  (20, lumberjack, 2),
  (30, storm, 3),
  (40, woodpecker, 2),
  (50, snow, 3),
  (60, spider, 2),
  (70, bird, 1),
  (80, rain, 3),
  (90, friend, 3),
  (100, sun, 1),
]

event_history = []

def can_trigger_event(event_name, cooldown):
  """
  Check if an event can be triggered based on its cooldown.
  """
  # Count the total number of events that have occurred
  total_events = len(event_history)

  # Get the last occurrence of the given event
  last_occurrence = next(
    (total_events - i - 1 for i, name in enumerate(reversed(event_history)) if name == event_name),
    None,
  )

  # If the event has never occurred, it can be triggered
  if last_occurrence is None:
    return True

  # Check if enough other events have occurred since the last occurrence
  return total_events - last_occurrence > cooldown



def pass_time(game_state:Game_State):
  """Action for passing time"""
  check_life(game_state)


  chance = get_lucky(game_state)

  # Iterate over the list to find the matching event
  for threshold, event, cooldown in events:
    event_name = event.__name__  # Use the function's name as the event identifier

    if chance <= threshold and can_trigger_event(event_name, cooldown):
      event(game_state)  # Trigger the event
      event_history.append(event_name)  # Add to event history
      break  # Stop checking once a match is found



def recover(game_state:Game_State):
  check_life(game_state)

  pass_time(game_state)



def grow(game_state:Game_State):
  """Action for growth"""
  check_life(game_state)

  text_path.set_current_text("testing")
  text_path.set_options([
    ("pass time", pass_time, None),
    ("grow again", grow, None),
  ])



def death(game_state:Game_State):
  text_path.set_current_text("No further actions are available. By age or decay, your life has met its end. Game Over.")
  text_path.set_options([
    ("Exit Game", exit_game, None),
  ])
  


'''
Bark - one-time against fire, 
Moss - one-time against snow, grows after rain
Fruit - animals
Flower - bugs
Nest - protection against lumberjack
Hydration - protection against fire, bad in the cold
Mushroom - protection against animals
'''



initial_dialogue = (
  "You are a lone tree. Winter is approaching. Do what you must to survive.",
  [
    ("Stand tall against the sands of time", fire, None),
    # ("Attend to growth", grow, None),
  ],
)

text_path = Text_Path(initial_dialogue)



def game_loop(stdscr:curses.window):

  # set up
  curses.curs_set(0)
  stdscr.nodelay(True)
  stdscr = curses.initscr()
  stdscr.clear()
  palette.init_colors()

  num_rows, num_cols = stdscr.getmaxyx()
  middle_row = int(num_rows / 2)
  middle_column = int(num_cols / 2)
  
  bg_window = curses.newwin(num_rows, num_cols, 0, 0)

  game_state = Game_State(bg_window)

  '''
  Title Screen
  '''
  
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

  