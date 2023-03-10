def filter_prime(list):
   list2 = []
   for num in list:
      prime = True
      if(num < 2):
         continue
      for j in range(2, num):
         if(num % j == 0):
            prime = False
      if prime:
         list2.append(num)
   return list2