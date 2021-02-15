'''
Code Up - Algorithm Basic - 100 Questions

[기초-삼향연산] 1063 Ternary Operator
https://codeup.kr/problem.php?id=1063

Date : 2021-01-30
Solved BY : TK Lee

Input : 

Receive integer
(-2147483648 ~ +2147483647)

123 456

Expected Output :

print larger value between two integer

456

'''
a, b = [int(x) for x in input().split()]
c = a if a > b else b
print(c)
