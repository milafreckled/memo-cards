import numpy
import time
def printDistances(distances, len1, len2):
    for i in range(len1 + 1):
        for j in range(len2+1):
            print(int(distances[i][j]), end=" ")
        print()
    return 0

def levenstein(s1, s2):
    distances = numpy.zeros((len(s1)+1, len(s2)+1))
    for i in range(len(s1)+1):
        distances[i][0]=i
    for j in range(len(s2)+1):
        distances[0][j]=j
    a = 0
    b = 0
    c = 0
    for i in range(1, len(s1)+1):
         for j in range(1, len(s2)+1):
             if s1[i-1] == s2[j-1]:
                 distances[i][j] = distances[i-1][j-1]
             else:
                 a = distances[i][j-1]
                 b = distances[i-1][j]
                 c = distances[i-1][j-1]
                 distances[i][j] = min(a, b, c)+1
    printDistances(distances, len(s1), len(s2))
    print(distances[len(s1)][len(s2)])

if __name__ == "__main__":
    print(f"Epoch starts {time.gmtime(0)}")
    a = time.perf_counter()
    levenstein("treba", "nebo")
    b = time.perf_counter()
    print(f"Time has ellapsed: {(b - a):0.4f} seconds")



