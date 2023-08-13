rules = """**Game Rules:**

Two players compete on a rectangular field containing randomly colored cells. Player A's home is located in the top-left corner, and Player B's home is in the bottom-right corner.

Players take turns making moves. A move consists of selecting a color from 8 possible options. However, it is prohibited to choose one's current color or the color of the opponent (i.e., only 6 colors are available for selection). After choosing a color, the player's home and all adjacent cells of the same color are painted with that chosen color. This becomes the player's territory. When repainting, cells adjacent to this territory with the new color are added to it. This allows the player to capture additional territory.

The player who captures the larger area by the time there are no more free cells wins the game.

You can customize the following:
* Field size (click "New Game" after making the selection)
* Who plays as Player A or B. It can be a human, a random algorithm (Level 1), or a greedy algorithm (Level 2). Changing the player takes effect immediately."""
