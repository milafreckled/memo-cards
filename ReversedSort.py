def cost(L):
    cost = 0
    for i in range(len(L)-1):
        j = L.index(min(L[i:len(L)]))
        print(L[i:j+1][::-1])
        rev = L[i:j+1][::-1]
        L = L[:i] + rev + L[j+1:]
        # rest = L[j+1:]
        print(L)
        # to_reverse.extend(rest)
  
        # L = to_reverse.copy()
        cost += (j - i + 1)

    return cost


T = int(input("Number of text cases: "))
for case in range(T):
    length = int(input())
    arr = list(map(int,input().strip().split()))[:length]
    
    # for i in range(length):
        # el = int(input())
        # arr.append(el)
    print(f'Case #{case+1}: {cost(arr)}\n')