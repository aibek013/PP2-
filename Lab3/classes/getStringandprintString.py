class String:
   def getString(self):
      self.input = input()

   def printString(self):
      print(self.input.upper())

string = String()
string.getString()
string.printString()  
