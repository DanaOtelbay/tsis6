#Write a Python function that checks whether a passed string is palindrome or not.

word = input()

def palindrome(word):
   re_word = ''.join(reversed(word))
   if re_word == word:
      return True
   else:
      return False

if palindrome(word):
   print("Palindrom")
else:
   print("Not palindrom")
