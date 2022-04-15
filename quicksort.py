def quicksort(array):
    length = len(array)
    if (length<=1):
        return array
    pivot = array.pop()
    less_pivot = []
    greater_pivot = []
    for num in array:
        if (num<= pivot):
            less_pivot.append(num)
        else:
            greater_pivot.append(num)
        

    return quicksort(less_pivot) + [pivot] + quicksort(greater_pivot)

length = input("Array length: ")
seq = []
for i in range(int(length)):
    num = input("Array["+str(i)+"]")
    seq.append(num)
   
print("\n")
print(seq)   
print(quicksort(seq))
