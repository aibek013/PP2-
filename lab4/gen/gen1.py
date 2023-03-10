def gen(n):
    idx = 0
    while idx < n:
        yield idx
        idx += 1
def square(seq):
    for i in seq:
        yield i ** 2

a = gen(n = int(input()))
b = square(a)
for i in b:
    print(i)