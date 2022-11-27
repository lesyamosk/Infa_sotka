def decorator(func):
    def wrapper(x,y):
        try:
            func(x,y)
        except BaseException:
            return 'error'
        return func(x,y)
    return wrapper

@decorator
def foo(a,b):
    return a/b

print(foo(9,0))
print(foo(16,2))