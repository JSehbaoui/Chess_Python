# Chess
This is a chess game implemented in python by using the libary pygame

## Motivation
I wanted to create a project in python for my computer science class that should be advanced but be doable for me on my own. I personaly enjoy chess alot, therefore I asked some advanced students if that would be possible for me to code and they encouraged me to do it.

## Goals
- This Chess game should be capable of any official chess rule by the end.
- Two players at the same PC should be able to play against each other.
- Implement a chess AI, rather by

    -importing an already existing, very advanced one [Stockfish](https://stockfishchess.org/) or [AlphaZero](https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go)
    - making my own

## Realization of the Game
I first of all created a parent class "Pieces" that would contain basic methods like moving or showing a piece.
Then I created a class for every other of the pieces, that would inherit for the parent "Pieces"

## Requirements for the current state
Use the package manager [pip](https://www.liquidweb.com/kb/install-pip-windows/) to install pygame.

```bash
pip install pygame
```

## How to play
For this, simply open main.py

Now by clicking at one of the pieces you can see where you can move it. By clicking at one of the marked tiles the piece will move to this square
You can exit the game by pressing ESC or by closing it as an usial window

## Bugs, I am aware of
- There is a bug where the tile under the king stays red after the check were denied
- If a knight check a king and the king wants to move, it ends in a recursive loop, and the game crashes.
- Sometimes you can't take a piece that is checking the king

## Missing features and rules
- The ["castling"-rule](https://en.wikipedia.org/wiki/Castling) from chess is missing
- The ["En passant"-rule](https://en.wikipedia.org/wiki/En_passant) from chess is missing
- The Player vs. AI mode is not available 
- The GUI features are not yet available

## Contribute?
It is currently not possible to collaborate on this project because the school requires a self made result

## Credits
I want to mention two people in this section. First of all Gero Beckmann. He was very kind by sometimes helping me out with the basic stucture of my code and motivated me to make this extra piece of work.
Lastly I want to also thank Vincent Piegsa, who worked on a similar project before. It was one of my inspirations to do this project to.
Gero and Vincent also showed me the way to work from different places without any issues using GIT and GITHUB. 
