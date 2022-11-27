def decorator(func):
    def wrapper(*args):
        A_inv = []
        n = len(args)
        for i in range (n-1,-1,-1):
            A_inv.append(args[i])
        return func(*A_inv)
    return wrapper

@decorator
def foo(*A):
    for i in A:
        print(i, end=' ')
foo(7,4,4,1,54,547,3,38,5,1,0,5)