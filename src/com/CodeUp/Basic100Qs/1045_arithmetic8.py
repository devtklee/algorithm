'''
Code Up - Algorithm Basic - 100 Questions

[기초-산술연산] 1045 Arithmetic - Add, Subtract, Multiply, Division, Reminder
https://codeup.kr/problem.php?id=1045

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive Two Integer

10 3

Expected Output :

First Line : Sum of two integer
Second Line : Substraction between two integer
Thrid Line : Mulitply two integer
Forth Line : Division (Integer only)
Fith Line : Division(Reminder only)
Sixth Line : Division

13
7
30
3
1
3.33

'''

x, y = input().split()

x = int(x)
y = int(y)

print(x+y)
print(x-y)
print(x*y)
print('%d' % (x/y))
print(x % y)
print('%.2f' % (x/y))
