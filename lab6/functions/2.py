def RealMadrid(s):
   upperletters = 0
   lowerletters = 0
   for i in s:
      if i.islower():
         lowerletters += 1
      if i.isupper():
         upperletters += 1
   return f"{upperletters}\n{lowerletters}" 
s = input()

print(RealMadrid(s))