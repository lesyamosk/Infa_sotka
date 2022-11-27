def decorator(func):
    def wrapper(*args):
        s= func(*args)
        print(args)
        return s
    return wrapper

@decorator
def foo(*A):
    for i in A:
        print(i+4, end=' ')
    print(end='\n')
foo(7,4,4,1,54,547,3,38,5,1,0,5)