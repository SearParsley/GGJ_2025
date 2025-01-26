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
  return min(random.randrange(50) + (random.random() * game_state.get_luck() * 3), 100)



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
    ("Protect yourself with your hardened barkskin", sacrifice_bark, game_state.has_resource("Bark")),
    ("Prevent major damage by releasing extra hydration", sacrifice_hydration, game_state.has_resource("Hydration")),
    ("Succumb to the inferno", burn, None),
  ])

def sacrifice_bark(game_state:Game_State):
  game_state.remove_resource("Bark")
  game_state.set_luck(game_state.get_luck() + 20)
  text_path.set_current_text("The fire burns through your sturdy bark, reducing it to ash, but the rest of you remains intact.")
  text_path.set_options([
    ("Continue with determination", brief_respite, None),
  ])

def sacrifice_hydration(game_state:Game_State):
  game_state.remove_resource("Hydration")
  game_state.set_luck(game_state.get_luck() + 10)
  text_path.set_current_text("The fire steams against your damp bark. You're not as hydrated, but nothing seems to have been damaged.")
  text_path.set_options([
    ("Do some photosynthesizing", increase_luck, None),
  ])

def burn(game_state:Game_State):
  for res in ["Acorn", "Moss", "Bark", "Nest", "Stick"]:
    game_state.remove_resource(res)
  
  game_state.set_health(game_state.get_health() - 40)

  text_path.set_current_text("The fire has harmed you gravely. All flammable resources have been burned away.")
  text_path.set_options([
    ("Try to recover what little you can", recover_event, None),
  ])



def lumberjack(game_state:Game_State):
  game_state.window.clear()

  ascii_axe = Text_Image('./ASCII/axe.txt', game_state.window, curses.color_pair(17))
  axe_x, axe_y = bg_center(ascii_axe, game_state)
  ascii_axe.draw(axe_x, axe_y - 2)
  ascii_handle = Text_Image('./ASCII/handle.txt', game_state.window, curses.color_pair(22))
  ascii_handle.draw(axe_x + 5, axe_y - 2)

  game_state.window.refresh()

  text_path.set_current_text("A burly man approaches, carrying a hatchet in his left hand. It looks like he's looking for lumber.")
  text_path.set_options([
    ("Stand firm and hope for the best", get_chopped, None),
    ("Command your fungi allies to release harmful spores upon the man", spores_lumberjack, game_state.has_resource("Mushroom")),
  ])

def get_chopped(game_state:Game_State):
  if game_state.has_resource("Bark"):
    game_state.remove_resource("Bark")
    game_state.add_resource("Stick")
    game_state.set_health(game_state.get_health() - 10)
    text_path.set_current_text("Although shattered into twigs, your bark proved a worthy opponent against the man's axe.")
  else:
    game_state.set_health(game_state.get_health() - 20)
    text_path.set_current_text("The beast of a man hacked into your core, leaving you with gashes that may not heal for many winters to come.")

  text_path.set_options([
    ("Attempt to mend your wounds", recover_event, None),
  ])

def spores_lumberjack(game_state:Game_State):
  game_state.window.clear()
  ascii_mushroom = Text_Image('./ASCII/mushroom.txt', game_state.window, curses.color_pair(22))
  mushroom_x, mushroom_y = bg_center(ascii_mushroom, game_state)
  ascii_mushroom.draw(mushroom_x, mushroom_y)
  game_state.window.refresh()

  text_path.set_current_text("The man first spats in surprise, then with disgust. He coughs, then turns quickly and departs.")
  text_path.set_options([
    ("Angle your leaves to maximize solar energy input", increase_luck, game_state.has_resource("Leaves")),
    ("Syphon nutrients from the mushrooms into your roots", consume_mushroom, game_state.has_resource("Mushroom")),
  ])

def consume_mushroom(game_state:Game_State):

  game_state.remove_resource("Mushroom")
  dmg = int(60 / get_lucky(game_state))
  game_state.set_health(game_state.get_health() - dmg)
  increase_luck(game_state)
  increase_luck(game_state)

  game_state.window.clear()
  ascii_mushroom = Text_Image('./ASCII/mushroom.txt', game_state.window, curses.color_pair(22))
  mushroom_x, mushroom_y = bg_center(ascii_mushroom, game_state)
  ascii_mushroom.draw(mushroom_x - 16, mushroom_y)
  ascii_tree = Text_Image('./ASCII/tree.txt', game_state.window, curses.color_pair(20))
  tree_x, tree_y = bg_center(ascii_tree, game_state)
  ascii_tree.draw(tree_x + 18, tree_y)
  game_state.window.refresh()

  text_path.set_current_text("Your roots knew of the toxins, but power often comes at a cost. The mushrooms are no more.")
  text_path.set_options([
    ("Overlook your small, yet glorious hill", brief_respite, None),
  ])



def storm(game_state:Game_State):
  text_path.set_current_text("storm prompt") # TODO: storm
  text_path.set_options([
    ("option 1", luck_event, None),
    ("option 2", recover_event, None),
  ])



def woodpecker(game_state:Game_State):
  game_state.window.clear()
  ascii_woodpecker = Text_Image('./ASCII/woodpecker.txt', game_state.window, curses.color_pair(17))
  woodpecker_x, woodpecker_y = bg_center(ascii_woodpecker, game_state)
  ascii_woodpecker.draw(woodpecker_x-3, woodpecker_y)
  ascii_trunk = Text_Image('./ASCII/trunk.txt', game_state.window, curses.color_pair(22))
  ascii_trunk.draw(woodpecker_x+3, woodpecker_y)
  game_state.window.refresh()

  text_path.set_current_text("A pesky woodpecker decides you're the perfect perch, and begins hammering into your side.")
  text_path.set_options([
    ("Offer it some grubs", sacrifice_grubs, game_state.has_resource("Grubs")),
    ("Do nothing", get_pecked, None),
  ])

def sacrifice_grubs(game_state:Game_State):
  game_state.remove_resource("Grubs")

  game_state.window.clear()
  ascii_woodpecker = Text_Image('./ASCII/woodpecker.txt', game_state.window, curses.color_pair(0))
  woodpecker_x, woodpecker_y = bg_center(ascii_woodpecker, game_state)
  ascii_trunk = Text_Image('./ASCII/trunk.txt', game_state.window, curses.color_pair(22))
  ascii_trunk.draw(woodpecker_x+3, woodpecker_y)
  game_state.window.refresh()

  text_path.set_current_text("The intruder quickly leaves after finding its dinner in your recesses.")
  text_path.set_options([
    ("Make some chlorophyll", recover_event, None),
    ("Meditate on the nature of stones", increase_luck, None),
  ])  

def get_pecked(game_state:Game_State):
  game_state.set_health(game_state.get_health() - 5)

  text_path.set_current_text("It feels anything but pleasant, but not much harm is done.")
  text_path.set_options([
    ("Contemplate the seasons", brief_respite, None),
  ])  



def snow(game_state:Game_State):
  text_path.set_current_text("snow prompt") # TODO: snow
  text_path.set_options([
    ("option 1", brief_respite, None),
    ("option 2", brief_respite, None),
  ])



def spider(game_state:Game_State):
  text_path.set_current_text("spider prompt") # TODO: spider
  text_path.set_options([
    ("option 1", brief_respite, None),
    ("option 2", brief_respite, None),
  ])



def bird(game_state:Game_State):
  text_path.set_current_text("bird prompt") # TODO: bird
  text_path.set_options([
    ("option 1", brief_respite, None),
    ("option 2", brief_respite, None),
  ])



def rain(game_state:Game_State):
  if not game_state.has_resource("Hydrated"): game_state.add_resource("Hydrated")

  game_state.window.clear()
  ascii_rain = Text_Image('./ASCII/rain.txt', game_state.window, curses.color_pair(24))
  rain_x, rain_y = bg_center(ascii_rain, game_state)
  ascii_rain.draw(rain_x, 0)
  game_state.window.refresh()

  text_path.set_current_text("Dark clouds crawl through the sky, coming to a halt in your proximity. It begins to rain.")
  text_path.set_options([
    ("Weather the storm", big_rain, None),
  ])

def big_rain(game_state:Game_State):
  if game_state.has_resource("Bark"):
    text_path.set_current_text("Your thick bark protects you from the frigid rain.")
    text_path.set_options([
      ("Revel in the downpour", luck_event, None),
    ])
  else:
    game_state.set_health(game_state.get_health() - 15)
    text_path.set_current_text("Without an outer protective layer, the frigid rain damages your roots.")
    text_path.set_options([
      ("Wait out the storm", brief_respite, None),
    ])



def friend(game_state:Game_State):
  text_path.set_current_text("friend prompt") # TODO: friend
  text_path.set_options([
    ("option 1", brief_respite, None),
    ("option 2", brief_respite, None),
  ])



def sun(game_state:Game_State):
  game_state.window.clear()
  ascii_sun = Text_Image('./ASCII/sun.txt', game_state.window, curses.color_pair(23))
  sun_x, sun_y = bg_center(ascii_sun, game_state)
  ascii_sun.draw(sun_x + 1, 4)
  game_state.window.refresh()

  text_path.set_current_text("The sun shines brightly overhead, showering you with delicious ultraviolet rays.")
  text_path.set_options([
    ("Convert those sweet rays into precious nutrients", absorb_rays, game_state.has_resource("Leaves")),
    ("Take the opportunity to sprout an acorn", gain_acorn, (game_state.has_resource("Hydrated") and not game_state.has_resource("Acorn"))),
    ("Simply bask in the sun's glory", recover_event, None),
  ])

def absorb_rays(game_state:Game_State):
  recover(game_state)
  recover(game_state)
  luck_event(game_state)

def gain_acorn(game_state:Game_State):
  game_state.window.clear()
  ascii_acorn = Text_Image('./ASCII/acorn.txt', game_state.window, curses.color_pair(16))
  acorn_x, acorn_y = bg_center(ascii_acorn, game_state)
  ascii_acorn.draw(acorn_x, acorn_y - 3)
  ascii_cap = Text_Image('./ASCII/cap.txt', game_state.window, curses.color_pair(22))
  ascii_cap.draw(acorn_x, acorn_y - 8)
  game_state.window.refresh()

  game_state.add_resource("Acorn")

  text_path.set_current_text("You have produced an acorn. Now all it needs is its own space to propagate.")
  text_path.set_options([
    ("Celebrate your new progeny", luck_event, None),
  ])



def recover(game_state:Game_State):
  addition = int(get_lucky(game_state) / 10)
  game_state.set_health(game_state.get_health() + addition)
  pass_time(game_state)

def recover_event(game_state:Game_State):
  recover(game_state)

  game_state.window.clear()
  ascii_tree = Text_Image('./ASCII/tree.txt', game_state.window, curses.color_pair(20))
  tree_x, tree_y = bg_center(ascii_tree, game_state)
  ascii_tree.draw(tree_x, tree_y)
  game_state.window.refresh()

  text_path.set_current_text("Recovery was successful.")
  text_path.set_options([
    ("Continue", pass_time, None),
  ])

  

def increase_luck(game_state:Game_State):
  addition = int(get_lucky(game_state) / 15)
  game_state.set_luck(game_state.get_luck() + addition)
  pass_time(game_state)

def luck_event(game_state:Game_State):
  increase_luck(game_state)

  game_state.window.clear()
  ascii_tree = Text_Image('./ASCII/tree.txt', game_state.window, curses.color_pair(20))
  tree_x, tree_y = bg_center(ascii_tree, game_state)
  ascii_tree.draw(tree_x, tree_y)
  game_state.window.refresh()

  text_path.set_current_text("Mother Nature smiles upon you.")
  text_path.set_options([
    ("Continue", pass_time, None),
  ])



def brief_respite(game_state:Game_State):
  game_state.window.clear()
  ascii_tree = Text_Image('./ASCII/tree.txt', game_state.window, curses.color_pair(20))
  tree_x, tree_y = bg_center(ascii_tree, game_state)
  ascii_tree.draw(tree_x, tree_y)
  game_state.window.refresh()

  text_path.set_current_text("You have a brief respite as time passes.")
  text_path.set_options([
    ("Continue", pass_time, None),
  ])



# List of (luck threshold, function, cooldown) tuples
events = [
  (fire, 3),
  (lumberjack, 3),
  # (storm, 3),
  (woodpecker, 2),
  # (snow, 3),
  # (spider, 2),
  # (bird, 2),
  (rain, 2),
  # (friend, 3),
  (sun, 1),
]

event_history = []

def can_trigger_event(event_name, cooldown):
  """Check if an event can be triggered based on its cooldown."""
  total_events = len(event_history)

  # Get the last occurrence of the given event
  last_occurrence = next(
    (total_events - i - 1 for i, name in enumerate(reversed(event_history)) if name == event_name),
    None,
  )

  if last_occurrence is None:
    return True  # Event can trigger if never occurred

  # Check if enough other events have occurred since the last occurrence
  return total_events - last_occurrence > cooldown



def pass_time(game_state:Game_State):
  """Action for passing time"""
  game_state.window.clear()

  chance = get_lucky(game_state)
  chance_gap = int(100 / len(events))

  # Try triggering an event based on chance
  for i, (event, cooldown) in enumerate(events):
    event_name = event.__name__  # Get the function name as event identifier

    if chance <= (i + 1) * chance_gap and can_trigger_event(event_name, cooldown):
      event(game_state)  # Trigger the event
      event_history.append(event_name)  # Add to event history
      break  # Stop checking once a match is found
  else:
    # If no event was triggered, select a random event
    event = random.choice(events)[0]
    event_name = event.__name__  # Get the event name
    event(game_state)  # Trigger the event
    event_history.append(event_name)  # Add to event history  





'''
Bark - one-time against fire, 
Moss - one-time against snow, grows after rain
Fruit - animals
Flower - bugs
Nest - protection against lumberjack
Hydration - protection against fire, bad in the cold
Mushroom - protection against animals
Stick - turns into nest
'''



initial_dialogue = (
  "You are a lone tree, atop a small hill. Mother Nature can be a cruel mistress. Do what you must to survive.         To follow a prompt, push the requisite numbered key.",
  [
    ("Stand tall against the sands of time", pass_time, None),
    # ("Attend to growth", grow, None),
  ],
)

text_path = Text_Path(initial_dialogue)

def game_loop(stdscr:curses.window):

  '''
  Set-up
  '''
  curses.curs_set(0)
  stdscr.nodelay(True)
  stdscr = curses.initscr()
  stdscr.clear()
  palette.init_colors()

  num_rows, num_cols = stdscr.getmaxyx()
  middle_row = int(num_rows / 2)
  middle_column = int(num_cols / 2)
  



  '''
  Title Screen
  '''
  
  title = Text_Image('./ASCII/title.txt', stdscr, curses.color_pair(16))
  title_x = middle_column - int(title.get_width() / 2) + 4
  title_y = middle_row - int(title.get_height() * 1) + 2

  instructions_text = "Press any button to start"
  instructions_x = middle_column - int(len(instructions_text) / 2) - 2
  instructions_y = middle_row + 4

  ascii_bug = Text_Image('./ASCII/bug.txt', stdscr, curses.color_pair(17))
  bug_x = 76
  bug_y = 15

  # draw title stuff
  title.draw(title_x, title_y)
  stdscr.addstr(instructions_y, instructions_x, instructions_text, curses.color_pair(17) | curses.A_BLINK)
  ascii_bug.draw(bug_x, bug_y)

  stdscr.refresh()
  
  while True:
    # wait for input
    key = stdscr.getch()
    if key != -1: break

    time.sleep(0.01)  # Small delay to reduce CPU usage



  '''
  Main Set-up
  '''

  stdscr.clear()
  stdscr.refresh()

  # Text box
  box_height = 10
  box_width = num_cols - 2
  box_y = num_rows - box_height
  box_x = 2
  text_box = Text_Box(box_height, box_width, box_y, box_x)

  bg_window = curses.newwin(num_rows, num_cols, 0, 0)
  game_state = Game_State(bg_window)

  game_state.window.clear()

  ascii_tree = Text_Image('./ASCII/tree.txt', game_state.window, curses.color_pair(20))
  tree_x, tree_y = bg_center(ascii_tree, game_state)
  ascii_tree.draw(tree_x, tree_y)

  game_state.window.refresh()

  # Display current text and options
  text_box.draw_box(text_path)

  key_state = None  # Track the current key state
  last_key_time = time.time()  # Timestamp of the last key press
  key_count = 0  # Count of valid key presses
  key_pressed = False  # Flag to track if key is pressed





  '''
  Dialogue loop
  '''

  in_dialogue = True
  dead = False

  while in_dialogue:
    key = stdscr.getch()  # Get the key (non-blocking)

    current_time = time.time()

    # Check if player is dead
    if game_state.get_health() <= 0 and not dead:  # If life reaches 0, declare player dead X.X
      dead = True
      text_path.set_current_text("No further actions are available. By age or decay, ascension or destruction, your life has met its end. Game Over.")
      text_path.set_options([
        ("Exit Game", exit_game, None),
      ])
      text_box.draw_box(text_path)

    if key != -1:  # A key is pressed
      if not key_pressed:  # Only process the key if not already pressed
        key_state = key  # Update the key state
        key_pressed = True  # Mark the key as pressed
        last_key_time = current_time  # Reset timestamp
        key_count += 1

        options = text_path.get_options()

        # Handle specific key presses
        if key_state == ord('q'):  # Quit the game
          break
        
        elif key_state in range(ord('1'), ord('1') + len(options)):
          # Choose dialogue option based on user input
          option_index = key_state - ord('1')
          text_path.choose_option(option_index, game_state)

          # Draw text box with current dialogue
          text_box.draw_box(text_path)

          options = text_path.get_options()
          if len(options) == 0: in_dialogue = False

    # Reset key state if no key is pressed for a short period
    if current_time - last_key_time > 0.2:  # 200ms debounce period
      key_pressed = False

    time.sleep(0.01)  # Small delay to reduce CPU usage



if __name__ == '__main__':    
  curses.wrapper(game_loop)

  