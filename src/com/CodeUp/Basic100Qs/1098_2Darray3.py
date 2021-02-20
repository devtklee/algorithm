'''
Code Up - Algorithm Basic - 100 Questions

[기초-2차원배열] 1098 Basic Alogrithm question - 2D Array
https://codeup.kr/problem.php?id=1098

Date : 2021-02-18
Solved BY : TK Lee

Youngil went to the amusement park with her parents
She got to see sugar confectionery (dissolving sugar to shape fish, etc.).

He puts several bars of different lengths on a grid, such as a checkerboard,

It was a game in which you picked up the number under the name of the sweets on the bar to get the sweets.
(Carp, crucian carp, dragon, etc. are written on it.)





Length of grid (h), width (w), number of bars (n), length of each bar (l),
The direction of placing the bar (d: 0 horizontally, 1 vertically) and
Given the leftmost or top position (x, y) of the bar to place the bar,

Let's create a program that prints out the shape of a bar that fills a grid.


input
In the first line, the vertical (h) and horizontal (w) of the grid are entered with a blank space,
Number of bars that can be placed in the second row (n)
From the third line, the length (l), direction (d), and coordinates (x, y) of each bar are entered.

The domain of the input value is as follows.

1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w


Print
Prints the state of the grid on which all bars are placed.
If it is covered by a bar, it is output as 1, otherwise it is output as 0.
However, each number is separated by a space and printed.


Input example
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5

Example output
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1

'''
h, w = [int(i) for i in input().split()]

# define board size
board = [[0 for col in range(w)] for row in range(h)]

# get number of stick
n = int(input())

# get information about each stick
for c in range(n):
    l, d, x, y = [int(i) for i in input().split()]
    x -= 1
    y -= 1

    for z in range(l):
        board[x][y] = 1
        if d == 0:  # horizontal
            y += 1
        else:  # Vertical
            x += 1

for j in range(h):
    for k in range(w):
        print(board[j][k], end=" ")
    print("")
