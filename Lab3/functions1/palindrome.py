def palindrome(string):
   string2 = string[:: -1]
   if string == string2:
      return True
   return False