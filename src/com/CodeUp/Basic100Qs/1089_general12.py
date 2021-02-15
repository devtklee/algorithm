'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1089 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1089

Date : 2021-02-15
Solved BY : TK Lee

A sequence of numbers according to a certain rule is called a series.

E.g
1 4 7 10 13 16 19 22 25 ... 
It is a sequence that starts with 1 and adds 3 to the previous number to create the next number.
In mathematics, the difference between the numbers before and after is the same

It is said to be a sequence of equal differences (the Chinese word for difference is the same).
Young-il, who learned of the sequence, suddenly became curious.

"So.... what's the 123rd number?"

Youngil wanted to create a program to automatically calculate a larger number.

When a starting value (a), an equal difference (d), and an integer (n) indicating the number of times are entered
Let's write a program that prints the nth number.

Input :

Accept starting value (a), difference (d), nth number (n) as integer (0 ~ 100)

1 3 5

Expected Output :

Print value of nth number in series

13

'''

a, d, n = [int(i) for i in input().split()]
print(a + (d * (n-1)))
