from time import sleep
@profile
def silnia(n): 
    if n < 2 and n > 0:
        return 1
    else:
        return n * silnia(n-1)


print(silnia(100))
