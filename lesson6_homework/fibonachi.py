N=int(input())
def fib(n):
    x1, x2 = 0, 1
    for __ in range(n):
        yield x1
        x1, x2 = x2, x1 + x2

for i in fib(N):
    print(i, end=' ')