'''
Code Up - Algorithm Basic - 100 Questions

[기초-2차원배열] 1099 Basic Alogrithm question - 2D Array
https://codeup.kr/problem.php?id=1099

Date : 2021-02-19
Solved BY : TK Lee

Youngil was interested in life science and was studying king ants.

While looking closely at the king ant, there was an ant that looked particularly sincere.
The ant came out of the anthill and traveled the fastest way to its prey.

The ant moved to the right, and when it encountered a wall, it moved downward and moved in the fastest way.
(If a road appears on the right, move to the right again.)

Youngil, who became curious about this, put the ant in a maze box and began to examine it.

The ants placed in the maze box will either find food or until they can no longer move.
It only moved to the right or down.

The structure of the maze box is given as 0 (where you can go), 1 (wall or obstacle),
Given a prey of 2, let's predict the path of a sincere ant.

However, if you arrive at the bottom right, if you can no longer move, if you find food,
Suppose you are no longer moving and staying there.


The maze box borders are all walled,
Since the anthill always exists at (2, 2), the ants start at (2, 2).


input
The structure of the maze box and the location of the food are entered.


Print
The path the sincere ant has traveled is marked as 9 and printed.


Input example
1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

Example output
1 1 1 1 1 1 1 1 1 1
1 9 9 1 0 0 0 0 0 1
1 0 9 1 1 1 0 0 0 1
1 0 9 9 9 9 9 1 0 1
1 0 0 0 0 0 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
size = 10

# Direction 0 : Move right
# Direction 1 : Move Down


def move(board, curRow, curCol, targetRow, targetCol):
    if (curRow == targetRow and curCol == targetCol):
        board[curRow][curCol] = 9
        return board
    else:
        if (curRow <= size and curCol <= size):
            board[curRow][curCol] = 9
            if (board[curRow][curCol+1] != 1):
                move(board, curRow, curCol+1, targetRow, targetCol)
            elif (board[curRow+1][curCol] != 1):
                move(board, curRow+1, curCol, targetRow, targetCol)
            else:
                return board


def printBoard(board):
    # output board
    for j in range(size):
        for k in range(size):
            print(board[j][k], end=" ")
        print("")

 # define board size
board = [[0 for col in range(size)] for row in range(size)]

# get information about row.
for row in range(size):
    board[row] = [int(i) for i in input().split()]

    # Find the location of food
    for col in range(size):
        if(board[row][col] == 2):
            destinationRow = row
            destinationCol = col

# Location of Ant (2,2) start to Move
move(board, 1, 1, destinationRow, destinationCol)

# Print Board
printBoard(board)
