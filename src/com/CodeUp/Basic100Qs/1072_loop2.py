'''
Code Up - Algorithm Basic - 100 Questions

[기초-반복실행구조] 1072 Loop
https://codeup.kr/problem.php?id=1072

Date : 2021-02-15
Solved BY : TK Lee

Input : 

Accept number of integers in first line, and list of numbers in second line

5
1 2 3 4 5

Expected Output :

Print numbers in seperated line.
But while( ), for( ), do~while( ) cant be used

1
2
3
4
5

'''


def printNumber(nums, idx, len):
    print(nums[idx])
    idx += 1

    if (len > idx):
        printNumber(nums, idx, len)
    else:
        exit


idx = 0
len = int(input())
nums = [int(n) for n in input().split()]

printNumber(nums, idx, len)
