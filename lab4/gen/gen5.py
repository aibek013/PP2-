def gen(n):
    while n >= 0:
        yield n
        n -= 1

gen1 = gen(n = int(input()))

for i in gen1:
    print(i)