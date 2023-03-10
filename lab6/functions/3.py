def palindromecheck(s):
   t = s[::-1]
   if t == s:
      return f"Yes"
   return "No"

    
s = input()
print(palindromecheck(s))