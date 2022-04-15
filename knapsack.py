arr = [[0 for _ in range(100)] for _ in range(100)]
w = []
v = [0]*10
result = 0
def KS (n, C):
    global arr
    global result
    if arr[n][C] != 0:
        return arr[n][C]
    if n==0 or C==0:
        result = 0
    elif w[n-1]>C:
        result = KS(n-1, C)
    else:
        tmp1 = KS(n-1, C)
        tmp2 = v[n-1] + KS(n-1, C-w[n-1])
    arr[n][C] = result
    return result

if __name__ == "__main__":
    
    n = int(input("How many items do you have?"))
    C = int(input("What is the knapsack capacity?"))
    for i in range(n):
        w.append(int(input('The weight of item #{}'.format(i))))
        v[i] = int(input('The value of item #{}'.format(i)))
        
    print("-"*20)
    knapsack = KS(n, C)
    print("The maximum value possible for your knapsack: "+str(knapsack))
