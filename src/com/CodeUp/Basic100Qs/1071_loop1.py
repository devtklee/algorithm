'''
Code Up - Algorithm Basic - 100 Questions

[기초-반복실행구조] 1071 Loop
https://codeup.kr/problem.php?id=1071

Date : 2021-02-15
Solved BY : TK Lee

Input : 

Input integers until 0 is entered.
(-2147483648 ~ +2147483647)

7 4 2 3 0 1 5 6 9 10 8

Expected Output :

Print integers in seperated line until 0 is entered.

7
4
2
3

'''

nums = [int(x) for x in input().split()]
idx = 0

while (nums[idx] != 0):
    print(nums[idx])
    idx += 1
