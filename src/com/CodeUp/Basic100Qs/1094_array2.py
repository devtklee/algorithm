'''
Code Up - Algorithm Basic - 100 Questions

[기초-1차원배열] 1094 Basic Alogrithm question - 1D Array
https://codeup.kr/problem.php?id=1094

Date : 2021-02-17
Solved BY : TK Lee

The information teacher calls a strange attendance before class begins.

To quickly learn the students' faces and names, the numbers are called randomly (randomly).
Young-il remembers the numbers the teacher called and wanted to try calling them backwards.

When you randomly call your attendance number n times, print the number you called in reverse.


Reference
You can write them in order in an array and print the recorded contents upside down.

example
int n, i;
int a[1000]={};
scanf("%d", &n); //Receive number input
for(i=1; i<=n; i++) //receive as many inputs
  scanf("%d", &a[i]); // Read and put them in the array in order.

for(i=n; i>=1; i--)
  printf("%d", a[i]); //Print the value stored in array i

input
In the first line, an integer n, which is the number of times the attendance number was called, is entered. (1 to 10000)
In the second line, n numbers (1 to 23) called randomly are entered in sequence with spaces.


Print
Change the order of the attendance numbers and print them with a blank space.


Input example
10
10 4 2 3 6 6 7 9 8 5

Example output
5 8 9 7 6 6 3 2 4 10

'''

l = int(input())
num = [int(i) for i in input().split()]

while (l != 0):
    print(num[l-1], end=" ")
    l -= 1
