'''
Code Up - Algorithm Basic - 100 Questions

[기초-반복실행구조] 1077 Loop
https://codeup.kr/problem.php?id=1077

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept 1 integer (0-100)

4

Expected Output :

print number from 0 to aceepted integer number

0
1
2
3
4

'''

start = 0
end = int(input())

while start <= end:
    print(start)
    start += 1
