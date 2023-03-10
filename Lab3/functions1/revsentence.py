def Reverse(string):
   string = string.split()
   list1 = list(string)
   list1.reverse()
   for i in list1:
      print(i, end = ' ')

Reverse("We are ready")