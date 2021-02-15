'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1091 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1091

Date : 2021-02-15
Solved BY : TK Lee

The sequence of numbers according to a certain rule is called a sequence.

E.g
1 -1 3 -5 11 -21 43 -85...
This is a sequence that starts with 1, multiplies the previous number by -2, and then adds 1 to create the next number.

Youngil, who learned of this strange sequence, became curious again.

"Then.... What is the 13th number?"

Young-il, of course, is very good at math, but he has rarely seen a problem like this...

So he wanted to create a program to automatically calculate a larger number.


When the starting value (a), the multiplying value (m), the adding value (d), and an integer (n) indicating the number of times are entered,
Let's write a program that prints the nth number.

Input :

Accept starting value (a), the multiplying value (m), the adding value (d), nth number (n) as integer (a, m, d (-50 ~ +50), n <=10)

1 -2 1 8

Expected Output :

Print value of nth number in series

-85

'''
a, m, d, n = [int(i) for i in input().split()]

while (n > 1):
    n -= 1
    a = a * m + d

print(a)
