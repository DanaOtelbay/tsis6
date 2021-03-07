#https://www.w3resource.com/python-exercises/python-functions-exercises.php
# ex 1

# a = list(map(int, input().split()))
# print(max(a))

a, b, c = input().split()

def max_number_of_two(a, b):
   if a > b: 
      return a
   return b

def max_number_of_three(a, b, c):
   return max_number_of_two(a, max_number_of_two(b, c))

ans = max_number_of_three(a, b, c)
print(ans)