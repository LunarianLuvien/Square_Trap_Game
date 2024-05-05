# Square Trap Game

## GENERAL INFORMATION

The Square Trap game is a strategy game played by two people. On the game board, there are 42 squares formed by 7 horizontal and 8 vertical lines. The game is played with 28 white and 28 black stones. The objective of the game is to reduce the opponent's number of stones to three.

The player with the white stones goes first. The player whose turn it is attempts to form a square by placing a stone at any intersection of the lines. Stones are placed alternately until all stones in hand are used up. No stones can be moved or played until all are placed.

After all stones are placed, players count the squares they have formed and remove the corresponding number of opponent’s stones from the game. If no player has formed a square, the first player (the one playing with white stones) removes one of the opponent’s stones from the game. At any stage of the game, while selecting an opponent's stone to be removed, formed squares cannot be disrupted.

Then, the player whose turn it is moves one of their stones to try to form a square. A stone can move horizontally or vertically as far as desired provided the path is clear, but jumping over other stones is not allowed in any circumstances. When a new square is formed, one opponent’s stone is removed. The player who reduces their opponent’s number of stones to three wins the game.

For an example of a game, see: [Example Game Video](https://youtu.be/4A1vGGDkAIg?t=178)

## PROBLEM DEFINITION

A program needs to be developed to simulate the Square Trap game described above. The game board must consist of at least 3 and at most 7 horizontal lines, and one more vertical line than the number of horizontal lines. Horizontal lines should be numbered, and vertical lines should be represented with uppercase letters (English letters only).

At the beginning of the game, the number of horizontal lines [3-7] should be obtained from the user, and an empty game board should be displayed.

Players should enter the position of their own stone they want to place on the game board or the position of the opponent’s stone they want to remove, by entering the number of the horizontal line (in the example [1-4]) and the letter of the vertical line (in the example [A-E]) consecutively (for example, 2D).

Similarly, players should enter the current position and the target position of their own stone they want to move, by leaving a space between the number of the current horizontal line and the letter of the vertical line and the number of the target horizontal line and the letter of the vertical line (for example, 3C 1C).

After each move that changes the game board, the game board should be displayed again. 
At the end of the game, the winning player’s color should be displayed on the screen.

### Notes:

- During data entry, the user’s incorrect or invalid data entries according to game rules, and data entries that might cause runtime errors (exception handling) should be controlled, and the user should be prompted until a valid entry is made. Additionally, data must always be taken in the specified order and manner.
- There is no need to handle situations where a player does not have a valid move according to game rules, such as when there are no stones of the opponent not inside a square, etc. In other words, it’s not necessary to handle cases where it’s the player's turn but no valid moves are available.


