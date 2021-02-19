'''
Code Up - Algorithm Basic - 100 Questions

[기초-2차원배열] 1097 Basic Alogrithm question - 2D Array
https://codeup.kr/problem.php?id=1097

Date : 2021-02-18
Solved BY : TK Lee

Young-il, who was waiting for her parents, was playing with black/white go boards stuffed and laid out...

I thought, "Shall we try to flip the ten (+) character?"

When all white stones (1) or black stones (0) are placed on the checkerboard (19 * 19),
Let's write a program that receives n coordinates and outputs the result of flipping the ten (+) characters.

Reference
If you use a two-dimensional array that can use horizontal and vertical numbers,
These forms can be easily recorded and used. Of course, you can also create an extended n-dimensional array.


example
int n, i, j, x, y;
int a[20][20]={};
for(i=1; i<=19; i++) //Receive checkerboard status input line by line
  for(j=1; j<=19; j++)
    scanf("%d", &a[i][j]);

scanf("%d", &n); //Get number of coordinates

for(i=1; i<=n; i++) //As many as the number of coordinates
{
  scanf("%d %d", &x, &y);
  for(j=1; j<=19; j++) // Replace horizontal line black <-> white
  {
    if(a[x][j]==0) a[x][j]=1;
    else a[x][j] = 0;
  }
  for(j=1; j<=19; j++) //replace vertical line black<->white
  {
    if(a[j][y]==0) a[j][y]=1;
    else a[j][y] = 0;
  }
}
...


input
The situation in which Go eggs are laid is input as an integer value of 19 * 19 size.
The number of times to flip the cross (n) is input.
The crosswise flip coordinates are input as many times as n. However, n is a natural number less than 10.


Print
Print the result of flipping the cross.


Input example
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
2
10 10
12 12

Example output
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''

array = [[0 for col in range(19)] for row in range(19)]

for n in range(19):
    array[n] = [int(i) for i in input().split()]

flipCnt = int(input())

for i in range(0, flipCnt):
    cord = input().split()
    point = list(map(int, cord))
    x = point[0]-1
    y = point[1]-1

    for j in range(0, 19):
        if array[x][j] == 0:
            array[x][j] = 1
        else:
            array[x][j] = 0

    for k in range(0, 19):
        if array[k][y] == 0:
            array[k][y] = 1
        else:
            array[k][y] = 0


for j in range(19):
    for k in range(19):
        print(array[j][k], end=" ")
    print("")
