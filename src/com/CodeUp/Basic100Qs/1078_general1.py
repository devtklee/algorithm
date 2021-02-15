'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1078 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1078

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept 1 integer (0-100)

5

Expected Output :

print sum of even number from 1 to aceepted integer number

6

'''

start = 1
end = int(input())
evenSum = 0

while start <= end:
    if(start % 2 == 0):
        evenSum += start
    start += 1

print(evenSum)
