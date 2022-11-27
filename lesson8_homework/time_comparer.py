import time


def time_decorator(func): #из конспектов
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        t=time.time() - start_time
        return res,t
    return wrapper

@time_decorator
def FIB_dinamic(n):
    if n<1:
        return
    A=[0, 1]+[0]*(n-1)
    for i in range(2, n+1):
        A[i] = A[i-1] + A[i-2]
    return A[n-1]

def FIB_recursion(n):
    if n < 1:
        return
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return FIB_recursion(n-1) + FIB_recursion(n-2)

@time_decorator
def fib_rec(n):
    return FIB_recursion(n)

res1, t1=fib_rec(30)
res2, t2=FIB_dinamic(30)
print('Рекурсия считает за ',t1, ' сек, а цикл - за ',t2, 'сек')