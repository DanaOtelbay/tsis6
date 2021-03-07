def pascal(n):
   list_pascal = [1]
   scope = [0]
   for row in range(max(n, 0)):
      print(*list_pascal)
      list_pascal = [a+b for a, b in zip(scope+list_pascal, list_pascal+scope)]

pascal(int(input()))