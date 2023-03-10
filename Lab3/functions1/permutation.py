from itertools import permutations

def permutation(string):
   res = [''.join(p) for p in permutations(string)]
   print(res, sep = ' ')
   
