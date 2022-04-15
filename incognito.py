def sumOfArray(arr):
    sum=0      
    for i in arr:
        sum = sum + i
            
    return(sum)    
def kochSnowflake(P, length, iterations):
    i=0
    while i<iterations:
        P = (4/3)* P
        i+=1
    return P
   
if __name__=="__main__":
    print(kochSnowflake(19683*3, 19683, 7))
    print(kochSnowflake(531441*3, 531441, 7))
    print(kochSnowflake(531441*3, 531441, 9))
    """
    N = int(input("Number of attributes: "))
    attrs = dict()
    solution = N
    for i in range(N):
        attr, category = input("Next attribute and category: ").split()
        if category in attrs:
            attrs[category].extend([attr])
        else:
            attrs[category] = [attr]
    store_attrs = []
    for key in attrs:
        store_attrs.append(len(attrs[key])) # saves length of attributes of one category
    for x in range((len(store_attrs)//2)+1):
        for y in range(x+1, len(store_attrs)):
            depth = y -x
            solution += store_attrs[x]*store_attrs[y]*depth
            
    print("Here is the solution: "+str(solution))
    """