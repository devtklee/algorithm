'''
Code Up - Algorithm Basic - 100 Questions

[기초-종합] 1092 Basic Alogrithm question - general
https://codeup.kr/problem.php?id=1092

Date : 2021-02-15
Solved BY : TK Lee

The online scoring system includes elementary school students, middle and high school students, college students, graduate students,
There are so many people coming in and solving problems, such as ordinary people, soldiers, programmers, and top coders.

Real-time scoring information can be viewed through the Judge Status menu.

character! Here... wait...
On the same day, 3 people who signed up at the same time enter the online scoring system and solve the problem.
Given that it's very regular, when is the day when we'll all solve the problem again?

For example, 3 people join/grade on the same day, and every 3 days, 7 days, and 9 days each
If you come in once, three people will solve the problem again after 63 days of signing up for the first time.


Suddenly a hint?

Doesn't it seem difficult for some reason?

Some people may have thought of the least common multiples learned in mathematics. But, learning and experiencing from information
The world of information science sometimes lends the power of computers to solve it in simple ways.

Read and understand the code below and try it out.

day is the number of days and a/b/c is the frequency of visits.
...
day=1;
while(day%a!=0 || day%b!=0 || day%c!=0) day++; //What does this mean?
printf("%d", day);
...

Of course, there can be so many different ways.

What is the correct answer to problem solving in information science?
It is not one, but all the ways to get accurate results with a given time/memory space.

Therefore, there is not only one correct answer to all problems.

There are many ways to think and try new, faster, and simpler methods.

Input :

On the same day, 3 people who signed up at the same time visit regularly,
The visit cycle is entered with a blank space. (However, the input value is a natural number less than 100.)

3 7 9

Expected Output :

Print out the day when all three of them visit again and solve the problem (how many days after joining/ranking up at the same time?).

63

'''

day = 1

a, b, c = [int(n) for n in input().split()]

while (day % a != 0 or day % b != 0 or day % c != 0):
    day += 1

print(day)
