#Write a Python function that takes a number as a parameter and check the number is prime or not.
#Check the number is prime or not
n = int(input())

def prime(n):
   for x in range(2, n):
      if n%x==0:
         return True

if prime(n):
   print("Number is prime")
else:
   print("Number is goooooood")