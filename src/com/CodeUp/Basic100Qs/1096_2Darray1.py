'''
Code Up - Algorithm Basic - 100 Questions

[기초-2차원배열] 1096 Basic Alogrithm question - 2D Array
https://codeup.kr/problem.php?id=1096

Date : 2021-02-17
Solved BY : TK Lee

In a school where they live in a dormitory, everyone returns home on some Fridays (everyone returns home).

Young-il, who went home after a long time, was thinking about the very big concave he had with his father.
He thought, "Can you program a stone on the board?"

If you put n white stones on a checkerboard (19 * 19),
Let's write a program that prints out the location of n white stones.


Reference
If you use a two-dimensional array that can use horizontal and vertical numbers,
These forms can be easily recorded and used. Of course, you can also create a wider n-dimensional array.

example
int n, i, j, x, y;
int a[20][20]={};
scanf("%d", &n);
for(i=1; i<=n; i++)
{
  scanf("%d %d", &x, &y);
  a[x][y]=1;
}
for(i=1; i<=19; i++) //one line (top to bottom)
{
  for(j=1; j<=19; j++) //one column (left to right) each
  {
    printf("%d", a[i][j]); // value output
  }
  printf("\n"); // line break
}


input
The number of white stones (n) to be placed on the board is entered in the first line.
The coordinates (x, y) to place the stone from the second line to the n+1 line are inputted in n lines.
n is a natural number less than 10, and x and y coordinates are from 1 to 19, and the same coordinates are not entered.


Print
Prints the situation of a board with white stones.
The location with white stones is 1, and 0 is output.


Input example
5
1 1
2 2
3 3
4 4
5 5

Example output
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''

np = int(input())
array = [[0 for col in range(19)] for row in range(19)]

for n in range(np):
    c, r = [int(i) for i in input().split()]
    array[c-1][r-1] = 1

for j in range(19):
    for k in range(19):
        print(array[j][k], end=" ")
    print("")
