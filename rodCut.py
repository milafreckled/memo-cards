

def rodCut(n, prices):
    # global maxPrice
    print(f'Running rodCut({n}, prices)')
    maxPrice = -1
    if n == 0:
        return 0
    for i in range(1, n+1):
        cost = prices[i - 1] + rodCut(n - i, prices)
        if cost > maxPrice:
            maxPrice = cost
        print(f'----Iteration: {i} ')
        print(f'----Max price now: {maxPrice}')
    return maxPrice
def knapsack(v, w, W):
    # table that will store result of subproblems:
    # row index corresponds to the current item and column – to knapsack capacity
    # therefore, T[i][j] will correspond to the maximum value that can be obtained using up to i-th item and having j capacity
    T = [[0 for i in range(W + 1)] for j in range(len(v) + 1)]
    # solving in bottom-up manner
    for i in range(1, v + 1):
        for j in range(W + 1):
            if w[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], T[i-1][j - w[i-1] + v[i-1])
    return T[len(v)][W]
### palindrome partitioning
def minCut(A):
    def isPalindrome(string):
        if string == string[::-1]:
            return True
        return False

    if len(A) == 1 or isPalindrome(A):
        return 0
    minCost = float('inf')
    for i in range(len(A) - 1, -1, -1):
        # m("abad"), m("aba") + 1
        cost = minCut(A[0:i]) + 1
        if cost < minCost:
            minCost = cost
    return minCost
        
if __name__ == "__main__":
    """
    lengths = [1, 2, 3, 4, 5, 6, 7, 8]
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rodLength = 4
    print(rodCut(rodLength, prices))
    """
    print(minCut("dVGAaVO25EmT6W3zSTEA0k12i64Kkmmli09Kb4fArlF4Gc2PknrlkevhROxUg"))