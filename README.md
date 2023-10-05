# Flappy Bird Game

A simple implementation of the classic Flappy Bird game using Python's Pygame library.

## How to Play

- Run the game by executing the script.
- Control the bird by pressing the **Spacebar** to make it jump.
- Navigate the bird through the pipes without colliding.
- Your score increases for every pipe passed.

## Prerequisites

Make sure you have Python and Pygame installed on your system. You can install Pygame using the following command:

```sh
pip install pygame
```

## How to Run

1. Clone the repository to your local machine.
2. Navigate to the project directory using the terminal or command prompt.
3. Run the following command:

```sh
python flappy_bird.py
```

## Controls

- **Spacebar:** Make the bird jump.

## Game Features

- The game window dimensions are 600x800 pixels.
- The bird falls due to gravity and can be controlled to jump upwards.
- Pipes move from right to left, and new pipes are generated as old ones go off the screen.
- The game keeps track of the player's score based on the number of pipes successfully passed.

## Dependencies

- Python 3.x
- Pygame

## Files

- `flappy_bird.py`: Contains the main game implementation.
- `images/bg.png`: Background image for the game.
- `images/base.png`: Image of the floor/base of the game.
- `images/bird1.png`: Image of the bird character.
- `images/pipe.png`: Image of the pipes used in the game.

## Acknowledgments

This game is built using the Pygame library, a set of Python modules designed for writing video games. Special thanks to the Pygame community for their contribution.

Have fun playing!