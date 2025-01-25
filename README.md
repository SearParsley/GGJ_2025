# GGJ_2025

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Game Controls](#game-controls)
5. [Credits](#credits)
6. [License](#license)

## Overview

TODO: Revise overview

This is a simple command-line game which I fully designed and created in 24 hours for the 2025 Global Game Jam. It was built using Python and the `curses` library.

You play as a tree, and must make branching (pun intended) decisions to survive as long as possible.

## Installation

### Prerequisites

- Python 3.x
- `curses` library (typically included with Python on Unix-like systems)
  
### Steps

1. Clone the repository:
  ```bash
  git clone https://github.com/SearParsley/GGJ_2025.git
  ```
2. Navigate to project directory:
  ```bash
  cd GGJ_2025
  ```
3. (Optional) Set up a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
4. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

Run the game with the following command:
```bash
python src/main.py
```

Make sure you are in the project directory (`GGJ_2025`)

### Exiting the Game

To exit the game, press `Q` or `Ctrl+C`

## Game Controls

TODO: Write controls

## Credits

### ASCII Art

I did make small edits to a few of the versions within the game, but  all the ones below are unmodified and linked to where I found them.

[Bug](https://ascii.co.uk/art/bug)
```
         / .'
   .---. \/
  (._.' \()
   ^"""^"
```

[Bee](https://asciiart.website/index.php?art=animals/insects/bees)
```
   ,-.
   \_/
  {|||)<
   / \
   `-'
```

[Mushroom](https://www.asciiart.eu/plants/mushroom)
```
           ___..._
      _,--'       "`-.
    ,'.  .            \
  ,/:. .     .       .'
  |;..  .      _..--'
  `--:...-,-'""\
          |:.  `.
          l;.   l
          `|:.   |
           |:.   `.,
          .l;.    j, ,
       `. \`;:.   //,/
        .\\)`;,|\'/(
         ` `itz `(,
```

[Axe](https://ascii.co.uk/art/axe)
```
   /'-./\_
  :    ||,>
   \.-'||
       ||
       ||
       ||   pjb
```

[Fire](https://ascii.co.uk/art/fire)
```
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

[Bird](https://asciiart.website/index.php?art=animals/birds%20(land))
```
                                               _,;
                        ,       .--.       _,-'.-;
        ,  "; /.-.       \`-, <j o. `._ ,-' ,'`_7
  `".__ |\   \\|/        <_  `-\ _       _,' _.'
  `'--.;\ ) .-.r_          <_`".| `\    `  _.>
      __.--'-\|/_)           <_ ;   \     _>
     `.__..--';.__.           `"     ;  ``
       /  `-'/| \_)\             \   |   \  mx
       |.-` (_/    \\             '|-. _  \
                  ./ y.__       _/ /     \ '.
         ,      ,'| ,--;.`".__  " "`      '\_>
         |`._  |  ;/.-.  `'--.;,--._       \>
         \_ .-. \/; |/.-.     /\-._.'`
         (_\|/.-..-.;f--'    | ; \ \`._
         __.;`'-'.\|/_)       \| |  `-.\  ,'|
     _.-(_/ |\ `-;';.__        '\;    ;| /  /
   '-.__.'  \_)   /|\\_)               \7,--.__
                 (_/ ;,                 ;-`.__.'
                      |\                 ( \
                      `-'                 \|
                                           `
```

[Spider](https://ascii.co.uk/art/bug)
```
    .  .       
   .|  |.      
   ||  ||      
   \\()//      
   .={}=.      
  / /`'\ \     
  ` \  / '   jv
     `'        
```

[Butterfly]()
```
      .-=-.   .-=-.
     ( 0   \V/   0 )
      \     O     /
       `.__ # __.'
        .'  #  '.
  jgs  (o  /#\  o)
        )/'   '\(
       (         )
```

[Dead Tree](https://www.asciiart.eu/plants/other)
```
                                                 .
                                     .         ;  
        .              .              ;%     ;;   
          ,           ,                :;%  %;   
           :         ;                   :;%;'     .,   
  ,.        %;     %;            ;        %;'    ,;
    ;       ;%;  %%;        ,     %;    ;%;    ,%'
     %;       %;%;      ,  ;       %;  ;%;   ,%;' 
      ;%;      %;        ;%;        % ;%;  ,%;'
       `%;.     ;%;     %;'         `;%%;.%;'
        `:;%.    ;%%. %@;        %; ;@%;%'
           `:%;.  :;bd%;          %;@%;'
             `@%:.  :;%.         ;@@%;'   
               `@%.  `;@%.      ;@@%;         
                 `@%%. `@%%    ;@@%;        
                   ;@%. :@%%  %@@%;       
                     %@bd%%%bd%%:;     
                       #@%%%%%:;;
                       %@@%%%::;
                       %@@@%(o);  . '         
                       %@@@o%;:(.,'         
                   `.. %@@@o%::;         
                      `)@@@o%::;         
                       %@@(o)::;        
                      .%@@@@%::;         
                      ;%@@@@%::;.          
                     ;%@@@@%%:;;;. 
                 ...;%@@@@@%%:;;;;,..    Gilo97
```

[Rose](https://www.asciiart.eu/plants/flowers)
```
                       .-~~~-
                  .-~~~_._~~~\   
                  /~-~~   ~.  `._ 
                 /    \     \  | ~~-_ 
         __     |      |     | |  /~\|
     _-~~  ~~-..|       ______||/__..-~~/
      ~-.___     \     /~\_________.-~~
           \~~--._\   |             /
            ^-_    ~\  \          /^
               ^~---|~~~~-.___.-~^
                 /~^| | | |^~\
                //~^`/ /_/ ^~\\
                /   //~||      \
                   ~   ||
            ___      -(||      __ ___ _
           |\|  \       ||_.-~~ /|\-  \~-._
           | -\| |      ||/   /  | |\- | |\ \
            \__-\|______ ||  |    \___\|  \_\|
      _____ _.-~/|\     \\||  \  |  /       ~-.
    /'  --/|  / /|  \    \||    \ /          |\~-
   ' ---/| | |   |\  |     ||                 \__|
  | --/| | ;  \ /|  /    -(||
  `./  |  /     \|/        ||)-
    `~^~^                  ||
```

[Tree](https://www.asciiart.eu/plants/other)
```
                * *    
             *    *  *
        *  *    *     *  *
       *     *    *  *    *
   * *   *    *    *    *   *
   *     *  *    * * .#  *   *
   *   *     * #.  .# *   *
    *     "#.  #: #" * *    *
   *   * * "#. ##"       *
     *       "###
               "##
                ##.
                .##:
                :###
                ;###
              ,####.
  /\/\/\/\/\/.######.\/\/\/\/\
```

[Fruits](https://ascii.co.uk/art/fruit)
```
  Apple:
  
   ,(.
  (   )
   `"'
  
  Pear:
  
    (
   / \
  (   )
   `"'
  
  Banana:
  
   ,
   \`.__.
    `._,'
  
  Orange:
  
   ,=.
  (.`:)
   `-'
  
  Lemon:
   ,.
  (:;)
   `'
  Grapes:
    \
   ()()
  ()()()
   ()()
    ()
  Peach:
   ,:.
  (:::)
   `-'
  Grapefruit:
   ,;:.
  (::;;)
   `;:'
  Pumpkin:
   ,).
  ((|))
   ``'
  Kiwi:
   _
  (:)
   "
  Tomato:
   ,v.
  ((  )
   `"'
  Pineapple:
   \|/
   AXA
  /XXX\
  \XXX/
   `^'
  Olive:
   /-\
  (   )
   `-'
  Peanut:
   ,+.
  ((|))
   )|(
  ((|))
   `-'
  Acorn:
   ,=|=.
  (XXXXX)
   |   |
   \   /
    `+'
  Coconut:
   ,+.
  //|\\
  |||||
  \\|//
   `+'
  chestnut:
   ,-"-.
  / ,-. \
  |(:::)|
  \ `-' /
   `-.-'
  
  -shimrod
```

[Acorn]()
```
            _
          _/-\_
       .-`-:-:-`-.
      /-:-:-:-:-:-\
      \:-:-:-:-:-:/
       |`       `|
       |         |
  jgs  `\       /'
         `-._.-'
            `
```

[Fly](https://ascii.co.uk/art/fly)
```
          _,_           __   __
       ._(@I@)_.       /  \-/  \
      .--{___}--.    ._\   |   /_.
      .-/  Y  \-.    .__\__Y__/__.
       /   |   \        _{___}_
  jgs  \__/-\__/       ' (@I@) '
                          ~^~
```

[Feather](https://ascii.co.uk/art/feather)
```
   ,
  "\",
  "=\=",
   "=\=",
    "=\=",
     "-\-"       ,---,
        \       _)   (_
  ldb    `     [__INK__]
 ```

[Dog]()
```
                  __
                 /\/'-,
         ,--'''''   /"
   ____,'.  )       \___
  '"""""------'"""`-----'
  pb
```

[Deer](https://ascii.co.uk/art/deer)
```
   ,_)/
     (-'
   .-'\ 
    "'\'"""""'),
       )/---,( 
  PjP / \  / |      , '     , '   , '   ,'   ,'    ,'   ;     ;
```

[Sun]()
```
      ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;  hjw
```

[Cat Eyes](https://ascii.co.uk/art/cat)
```
    _.---.._             _.---...__
  .-'   /\   \          .'  /\     /
  `.   (  )   \        /   (  )   /
    `.  \/   .'\      /`.   \/  .'
      ``---''   )    (   ``---''
              .';.--.;`.
            .' /_...._\ `.
          .'   `.a  a.'   `.
         (        \/        )
          `.___..-'`-..___.'
             \          /
              `-.____.-'  Felix Lee 
```

[Campfire](https://ascii.co.uk/art/campfire)
```
             (                 ,&&&.
              )                .,.&&
             (  (              \=__/
                 )             ,'-'.
           (    (  ,,      _.__|/ /|
            ) /\ -((------((_|___/ |
          (  // | (`'      ((  `'--|
        _ -.;_/ \\--._      \\ \-._/.
       (_;-// | \ \-'.\    <_,\_\`--'|
       ( `.__ _  ___,')      <_,-'__,'
  jrei  `'(_ )_)(_)_)'
```

[Beehive](https://ascii.co.uk/art/bee)
```
      ^^      .-=-=-=-.  ^^
  ^^        (`-=-=-=-=-`)         ^^
          (`-=-=-=-=-=-=-`)  ^^         ^^
    ^^   (`-=-=-=-=-=-=-=-`)   ^^                            ^^
        ( `-=-=-=-(@)-=-=-` )      ^^
        (`-=-=-=-=-=-=-=-=-`)  ^^
        (`-=-=-=-=-=-=-=-=-`)              ^^
        (`-=-=-=-=-=-=-=-=-`)                      ^^
        (`-=-=-=-=-=-=-=-=-`)  ^^
         (`-=-=-=-=-=-=-=-`)          ^^
          (`-=-=-=-=-=-=-`)  ^^                 ^^
      jgs   (`-=-=-=-=-`)
             `-=-=-=-=-`
```

## Licence

TODO: Choose license

