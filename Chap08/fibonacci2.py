d = [0] * 100
d[1] = 1
d[2] = 1

def fibo(x):
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))