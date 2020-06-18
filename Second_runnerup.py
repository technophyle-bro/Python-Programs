#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up. Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
#use split function

n = int(input())
numb = input()
lis = list(map(int, numb.split()))
big, sbig = -100, -100
for i in lis:
    if (i > big):
        big, sbig = i, big
    elif (i < big and i > sbig):
        sbig = i
print (sbig)