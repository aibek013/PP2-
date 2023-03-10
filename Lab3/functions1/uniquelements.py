def unique(nums):
   list = []
   for x in nums:
      if x not in list:
         list.append(x)
   for x in list:
      print(x)

unique([1,2,2,3,4,5,6,5,4,3,3])