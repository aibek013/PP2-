def gen(n):
    idx = 0
    while idx < n:
      yield idx
      idx += 1

def cr7(seq):
   for i in seq:
      if i % 3 == 0:
         if i % 4 == 0:
            yield i

a = gen(n = int(input()))
b = cr7(a)
for i in b:
    print(i)