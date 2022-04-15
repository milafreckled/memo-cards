from time import sleep

@profile
def silnia(n):
    res = 1
    for i in range (1, n+1):
        res = res*i
    print(res)


silnia(100)

