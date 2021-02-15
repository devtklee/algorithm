'''
Code Up - Algorithm Basic - 100 Questions

[기초-반복실행구조] 1073 Loop
https://codeup.kr/problem.php?id=1073

Date : 2021-02-15
Solved BY : TK Lee

Input :

Accept number of integers until 0 is entered.

Excepted order :
    1. Check condition
    2. Execute code block
    3. check condition again
    4. Execute code block

7 4 2 3 0 1 5 6 9 10 8

Expected Output :

Print numbers in seperated line.

7
4
2
3

'''

nums = [int(n) for n in input().split()]
idx = 0
q = 1

while q != 0:
    if(nums[idx] != 0):
        print(nums[idx])
        idx += 1
    else:
        q = 0
        exit
