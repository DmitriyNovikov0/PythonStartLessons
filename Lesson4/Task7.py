def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= n
        yield a

for el in fact(10):
    print(el)