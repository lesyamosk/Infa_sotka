from random import randint
a=list(map(int, input().split()))
def Hoar_sort(a, left, right):
    if left >= right:
        return
    i, j = left, right
    x = a[randint(left, right)]
    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] =a[j], a[i]
            i +=1
            j -=1
    Hoar_sort(a, left, j)
    Hoar_sort(a, i, right)
Hoar_sort(a,0,len(a)-1)
print(*a)