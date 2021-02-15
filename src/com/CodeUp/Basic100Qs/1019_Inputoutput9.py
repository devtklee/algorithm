'''
Code Up - Algorithm Basic - 100 Questions

[기초-입출력] 1019 Input/Output - Print Date
https://codeup.kr/problem.php?id=1019

Date : 2021-01-28
Solved BY : TK Lee

Input : 

Year, Month, day will be entered sepearted by "."

2013.8.5

Expected Output :

Print year, month, day as yyyy.mm.dd format

2013.08.05

Approach :

%02d means integer type will be always 2 digits. If only one integer, print 0 in the beginning.

'''

y, m, d = [int(i) for i in input().split('.')]
print("%04d.%02d.%02d" % (y, m, d))
