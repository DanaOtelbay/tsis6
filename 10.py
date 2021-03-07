#Write a Python program to print the even numbers from a given list
"""
a = list(map(int, input().split()))

b = list(filter(lambda a: a%2==0, a))

print(b)
"""

a = list(map(int, input().split()))

def even_number(a):
   ans = []
   for n in a:
      if n%2==0:
         ans.append(n)
   return ans

print(even_number(a))