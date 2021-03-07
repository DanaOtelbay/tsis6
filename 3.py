a = list(map(int, input().split()))

# def mult_of_number(a):
#    ans = 1

#    for i in range(len(a)):
#       ans *= a[i]

#    return ans

# print(mult_of_number(a))

import functools

print(functools.reduce(lambda x, y: x*y, a))