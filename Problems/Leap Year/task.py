'''
Write a program that checks if a year is leap.

A year is considered leap if it is divisible by 4 and NOT divisible by 100, or if it is divisible by 400. So, 2000 is leap and 2100 isn't.

Output either "Leap" or "Ordinary" depending on the input.

Sample Input 1:

2100
Sample Output 1:

Ordinary
Sample Input 2:

2000
Sample Output 2:

Leap
'''

year = int(input())
print("Leap" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Ordinary")
