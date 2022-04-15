def Merge(A, aux, low, mid, high):
    k = low
    i = low
    j = mid+1
    while i<=mid and j<=high:
        if A[i]<A[j]:
            aux[k] = A[i]
            k=k+1
            i=i+1
        if A[i]>A[j]:
            aux[k] = A[j]
            k=k+1
            j=j+1

    while i<=mid:
        aux[k] = A[i]
        k=k+1
        i=i+1

    for i in range(low, high+1):
        A[i] = aux[i]
        


def mergesort(A, aux, low, high):
    if low==high:
        return

    mid = (low + ((high - low)>>1))
    mergesort(A, aux, low, mid)
    mergesort(A, aux, mid+1, high)
    Merge(A, aux, low, mid, high)

def isSorted(A):
    prev = A[0]
    for i in range(1, len(A)):
        if A[i]<prev:
            print("MergeSort fails!")
            return False
        prev = A[i]
    return True

if __name__ == '__main__':
    A = [1, 8, 0, 5, 4, 7, -2]
    aux = A.copy()
    

    mergesort(A, aux, 0, len(A)-1)
    if (isSorted(A)):
        print(A)
