# Two-Player Pygame Chess

## Overview
This is a two-player chess game implemented in Python using the Pygame library. The game features all standard chess pieces, valid move checks for each piece, and a graphical user interface for an engaging gaming experience.

## Features
- Two-player mode: Play as either white or black pieces.
- Graphical interface: Visual representation of the chessboard and pieces.
- Valid move checks: Ensures that only legal moves are allowed for each piece.
- Check and Checkmate detection: Highlights the king in check.
- Game over detection: Declares the winner when the game ends.
- Forfeit option: Players can forfeit the game by clicking the "FORFEIT" button.

## Requirements
- Python 3.x
- Pygame

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install Pygame using pip:
    ```sh
    pip install pygame
    ```

## How to Run
1. Clone the repository or download the source code files.
2. Navigate to the directory containing the files.
3. Run the Python script:
    ```sh
    python chess.py
    ```

## Files
- `chess.py`: The main script containing the game logic and Pygame setup.

## Game Controls
- **Mouse**: Click to select and move pieces.
- **Keyboard**: Press `Enter` to restart the game after it ends.

## Code Structure
### Variables and Initialization
- Initialize Pygame, set up display, and load fonts.
- Define game variables and load piece images.

### Drawing Functions
- `draw_board()`: Draws the chessboard and UI elements.
- `draw_pieces()`: Draws the pieces on the board.
- `draw_valid()`: Highlights valid moves for the selected piece.
- `draw_captured()`: Displays captured pieces.
- `draw_check()`: Highlights the king in check.
- `draw_game_over()`: Displays game over screen.

### Move Validation Functions
- `check_options()`: Checks all valid moves for pieces.
- `check_king()`, `check_queen()`, `check_bishop()`, `check_rook()`, `check_pawn()`, `check_knight()`: Individual functions for validating moves of each piece.
- `check_valid_moves()`: Checks valid moves for the selected piece.

### Main Game Loop
- Handles game logic, including piece selection, move validation, capturing pieces, and turn management.
- Detects game over conditions and handles restarting the game.

## Credits
This game was developed using Python and Pygame. 

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or feedback, please contact [your email or GitHub profile].
