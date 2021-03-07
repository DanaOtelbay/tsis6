#Write a Python function to check whether a number is perfect or not.

n = int(input())

divisirs = []

for x in range(1, n):
   if n%x==0:
      divisirs.append(x)

summa = sum(divisirs)
divisirs.append(n)
half_sum = int(sum(divisirs)/2)
if summa==n and half_sum==n:
   print("Perfect")
else:
   print("nooooo broooo")