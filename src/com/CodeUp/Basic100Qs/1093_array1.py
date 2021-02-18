'''
Code Up - Algorithm Basic - 100 Questions

[기초-1차원배열] 1093 Basic Alogrithm question - 1D Array
https://codeup.kr/problem.php?id=1093

Date : 2021-02-17
Solved BY : TK Lee

The information teacher calls a strange attendance before class begins.

The teacher looks at the attendance book and calls the number.
To quickly learn the students' faces and names, the numbers are called randomly (randomly).

And students whose faces and names are not well remembered call the number multiple times.
They are trying to quickly learn their name and face.

Let's print out the number of times each number (1 ~ 23) was called when randomly called the attendance number n times.


Reference
You can also declare 23 variables to record and print the number of times each number is called.
However, in the C language, you can use an array that uses the same name and number.
This is like identifying houses by numbering them like the number of buildings in an apartment (for example, building a 101).
Similar.

For example, if building a 101 is expressed differently, it can be expressed as a[101].
To use an array, which is a variable that can store data by numbering like this,
Like a variable, it must be declared before use, but it is possible in the following way.

example
int a[100]; //Create an array that can hold integers from a[0] to a[99].
for(i=0; i<100; i++)
{
  scanf("%d", &a[i]); // Repeat each room in order and enter values.
}

It is good to initialize the values ​​in the array before using it.
There are several ways to do this:

int a[24]={}; // All values ​​from 0 to 23 are initialized to 0.
int a[24]={1,2,3}; //1,2,3 are entered in this order, and all others are initialized to 0.
int a[3]={1,2,3}; //1,2,3 are stored in order.
int a[3]={1,2,3,4}; //Create 3 rooms and put in 4 values? An error occurred!


Reference code for troubleshooting

int n, i, t;
int a[24]={};
scanf("%d", &n); //Get number input
for(i=1; i<=n; i++) // receive as many inputs
{
  scanf("%d", &t); // read
  a[t]=a[t]+1; // Add 1 to the existing value and save again. Same as a[t]+=1.
}
for(i=1; i<=23; i++)
{
  printf("%d", a[i]); //Print the values ​​stored in arrays 1~23
}


input
In the first line, an integer n, which is the number of times the attendance number was called, is entered. (1 to 10000)
In the second line, n numbers (1 to 23) called randomly are entered in sequence with spaces.


Print
The number of times the number is called from No. 1 is sequentially separated by spaces and output as one line.


Input example
10
1 3 2 2 5 6 7 4 5 9

Example output
1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0

'''

l = int(input())
num = [int(i) for i in input().split()]
numCnt = [0 for j in range(23)]
cnt = 0

for n in num:
    numCnt[n-1] += 1

for nc in numCnt:
    print(nc, end=" ")
