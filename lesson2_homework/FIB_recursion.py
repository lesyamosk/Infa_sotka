def FIB_recursion(n):
    if n < 1:
        return
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return FIB_recursion(n-1) + FIB_recursion(n-2)