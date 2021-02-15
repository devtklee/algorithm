'''
Code Up - Algorithm Basic - 100 Questions

[기초-삼향연산] 1064 Ternary Operator
https://codeup.kr/problem.php?id=1063

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive integer
(-2147483648 ~ +2147483647)

3 -1 5

Expected Output :

print most least number

-1

'''
a, b, c = [int(x) for x in input().split()]

x = a if (b > a and c > a) else (b if c > b else c)
print(x)
