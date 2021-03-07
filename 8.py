#Write a Python function that takes a list and returns a new list with unique elements of the first list.

#print(set(map(int, input().split())))

a = list(map(int, input().split()))

def unique_list(a):
   ans = []
   for n in a:
      if n not in ans:
         ans.append(n)
   return ans

print(unique_list(a))