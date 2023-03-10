def gen(n):
    idx = 0
    while idx < n:
      yield idx
      idx += 1

def iseven(seq):
   for i in seq:
      if i % 2 == 0 and i != 0:
         yield i

a = gen(n = int(input()))
b = iseven(a)
for i in b:
    print(i)