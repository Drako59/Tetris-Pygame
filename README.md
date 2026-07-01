# Tetris Pygame

A classic Tetris-style game built with Python and Pygame.  
This was created as an early learning project to practice Python, game loops, collision detection, keyboard input, and basic game logic with Pygame.

## Overview

The game recreates the main mechanics of Tetris: falling blocks, movement, rotation, row clearing, scoring, increasing speed, sound effects, and a game-over screen.

The project is written in Python and uses Pygame for rendering, keyboard handling, sounds, and the main game loop.

## Features

- Classic falling-block gameplay.
- Random tetromino generation.
- Movement left, right, and down.
- Block rotation.
- Hard drop.
- Row clearing.
- Score system.
- Level/speed progression.
- Background music and sound effects.
- Game-over screen.
- Dynamic board size based on the display size.

## Tech Stack

- Python
- Pygame

## Project Structure

```text
Tetris-Pygame/
├── Tetris/
│   ├── Tetris .py          # Main game file
│   └── Sounds/             # Music and sound effects
├── .idea/                  # IDE project files
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Drako59/Tetris-Pygame.git
cd Tetris-Pygame/Tetris
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install Pygame:

```bash
pip install pygame
```

## Running the Game

Run the game from inside the `Tetris` folder:

```bash
python "Tetris .py"
```

Running from inside the `Tetris` folder is important because the game loads sound files from the local `Sounds` directory.

## Controls

| Key | Action |
| --- | --- |
| Left Arrow | Move block left |
| Right Arrow | Move block right |
| Down Arrow | Move block down faster |
| Up Arrow / Z | Rotate block |
| Space | Hard drop |
| M | Mute / unmute music |
| Esc | Pause / resume |

## Game Mechanics

- The board is represented as a 2D grid.
- Each tetromino is made from four Pygame rectangles.
- Collision checks prevent blocks from moving outside the board or through placed blocks.
- Full rows are removed and the blocks above them move down.
- Clearing rows increases the score.
- Clearing four rows gives a larger bonus.
- The falling speed increases as the score grows.

## Notes

This is an early learning project, so some parts of the code are experimental and can be improved. The purpose of the project was to learn how to build a full playable game using Python and Pygame.

## Possible Future Improvements

- Split the code into multiple files/classes.
- Add a start menu and restart button.
- Add a next-piece preview.
- Add hold-piece support.
- Save high scores.
- Improve rotation logic with wall kicks.
- Add a requirements file.
- Add screenshots or gameplay GIFs to the README.

## License

No license has been added yet.
