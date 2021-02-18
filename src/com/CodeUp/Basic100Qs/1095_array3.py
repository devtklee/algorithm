'''
Code Up - Algorithm Basic - 100 Questions

[기초-1차원배열] 1095 Basic Alogrithm question - 1D Array
https://codeup.kr/problem.php?id=1095

Date : 2021-02-17
Solved BY : TK Lee

The information teacher calls odd attendance today.

Youngil tried to think differently today.
I don't think I have all the attendance numbers... What was the fastest number?

When the attendance number is called at random n times, let's print out the earliest number.


Reference
If you write them in order in an array, you can check all the recorded contents to find the smallest value.

By the way, how do you compare and find the smallest value?


input
The number of times the number was called (n, 1 ~ 10000) is entered in the first line.
n random numbers (k, 1 to 23) are entered in order with a space in the second line.


Print
Only one of the numbers that called for attendance is output.


Input example
10
10 4 2 3 6 6 7 9 8 5

Example output
2

'''

l = int(input())
num = [int(i) for i in input().split()]

minNum = num[0]

for n in num:
    if(minNum >= n):
        minNum = n

print(minNum)
