# Branching Out

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Game Controls](#game-controls)
5. [Credits](#credits)
6. [License](#license)

## Overview

This is a simple command-line game which I fully designed and created in 24 hours for the 2025 [Global Game Jam](https://globalgamejam.org/), hosted by my [university](https://globalgamejam.org/jam-sites/2025/utah-state-university). It was built using Python and its `curses` library, in addition to ASCII assets available online (with some edits).

You play as a lone tree, and you must make branching (pun intended) decisions to survive in this world. Your choices will impact what options are available for you in the future.

In the current (demo) build, there is no 'win' condition, but reaching 0 health will result in a game over. My current plan for a future win condition is to propagate a seed and nurture it into a sapling. But for now, we just keep going through available events until you quit or die.
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

## Usage

Run the game with the following command:
```bash
python src/main.py
```

Make sure you are in the project directory (`GGJ_2025`)

### Exiting the Game

To exit the game, press `Q` or `Ctrl+C`

## Game Controls

The controls are very simple. Each text box will have a message followed by one or more numbered options. To choose an option, simply press the key of the number associated with that option. For example, I would press the `2` key to select option number 2.

## Credits

### ASCII Art

Many of the in-game versions have been modified to fit my needs, but each of the ASCII images shown below is unmodified. While the origin of many ASCII images may be lost to time, I provide a link to where I was able to find each image.

[Bug](https://ascii.co.uk/art/bug)
```
         / .'
   .---. \/
  (._.' \()
   ^"""^"
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

[Acorn](https://ascii.co.uk/art/acorn)
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

[Sun](https://www.asciiart.eu/nature/sun)
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

[Rain](https://www.asciiart.eu/nature/rains)
```
          ------               _____
         /      \ ___\     ___/    ___
      --/-  ___  /    \/  /  /    /   \
     /     /           \__     //_     \
    /                     \   / ___     |
    |           ___       \/+--/        /
     \__           \       \           /
        \__                 |          /     There are holes in the sky,
       \     /____      /  /       |   /     Where the rain gets in,    
        _____/         ___       \/  /\      The holes are very small,  
             \__      /      /    |    |     That's why rain is thin.   
           /    \____/   \       /   //                                 
       // / / // / /\    /-_-/\//-__-            - Spike Milligan       
        /  /  // /   \__// / / /  //
       //   / /   //   /  // / // /
        /// // / /   /  //  / //
     //   //       //  /  // / /
       / / / / /     /  /    /
    ///  / / /  //  // /  // //
       ///    /    /    / / / /
  ///  /    // / /  // / / /  /
     // ///   /      /// / /
```
### Unused Assets (For Now)

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

[Bee](https://asciiart.website/index.php?art=animals/insects/bees)
```
   ,-.
   \_/
  {|||)<
   / \
   `-'
```

[Dog](https://ascii.co.uk/art/dog)
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

## Licence

[MIT license](https://mit-license.org/)
