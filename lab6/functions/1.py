def product_of_list(list):
   result = 1
   for i in list:
      result *= i
   return result

print(product_of_list([1,2,3,4,5]))