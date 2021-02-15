'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1087 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1087

Date : 2021-02-15
Solved BY : TK Lee

When program add integers like 1, 2, 3 ...,  
write a code to add numbers until sum is less than input number.

Input :

Accept integers (i <= 100,000,000)

57

Expected Output :

Add integers until sum of integer is greater or equal to input value and print sum.

66

'''

i = int(input())
cnt = 1
sum = 1

while (i > sum):
    cnt += 1
    sum += cnt

print(sum)
