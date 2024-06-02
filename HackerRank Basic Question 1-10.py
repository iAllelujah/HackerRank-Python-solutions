#Q1.
"""Given an integer n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird"""  
#SOLUTIONS
"""def Weird_Or_Not():
    if n%2!=0:
        print("Weird")
    elif n%2==0 and n in range(2,5):
        print("Not Weird")
    elif n%2==0 and n in range(6,21):
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")

n=int(input("Enter a number"))
Weird_Or_Not()"""

#Q2.
"""The provided code stub reads two integers from STDIN, a and b
Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""
#SOLUTION
"""a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))

def Three():
    print(a+b)
    print(a-b)
    print(a*b)

Three()"""

#Q3.
"""The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,
a//b. The second line should contain the result of float division, a/b. """

#SOLUTION
"""def Devision():
    print(a//b)
    print(a/b)

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
Devision()"""

#Q4.
"""The provided code stub reads and integer n from STDIN. For all non-negative integers i<n, print i^2. """
#SOLUTION
"""i=0
n=int(input("Enetr a number"))
while i<n+1:
    print(i**2)
    i+=1"""

#5.
"""The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
1,2,4....n"""
#SOLUTION
"""n = int(input())
result=""
for i in range(1, n+1):
    result+=str(i)
    print(result)"""

#6.
"""Complete the print_full_name function in the editor below.
Print_full_name has the following parameters:
string first: the first name
string last: the last name
Prints
string: 'Hello! You just delved into python' where and are replaced with and . """
#SOLUTION
"""def print_FullName(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
print_FullName(input("Enter first name"),input("Enter last name"))"""