import math
import random

def kochSnowflake(length, iterations):
    P = 3*length
    i=0
    while i<iterations:
        P = (4/3)* P
        i+=1
    return P
def kochSnowflakeSq(length, iterations):
    P = 4*length
    i=0
    while i<iterations:
        P = (5/3)* P
        i+=1
    return P

def turnRadius(wb, sa):
    return round(wb/math.sin((math.pi/180)*sa), 2)
   
if __name__=="__main__":
    size = int(input("Your array size: "))
    print(f'Your array will be {size}x{size} size')
   # user_input = input(f'Give {size*size} numbers, separated by comma: ')
    arr = []
    for i in range(size*size):
        new_el = random.randrange(10)
        arr.append(new_el)
    twod_arr = []

    for x in range(size):
        column_elements = []
        for y in range(x, x+size):
            column_elements.append(arr[(x+y)])
        twod_arr.append(column_elements)
        
    print(arr)
    print(twod_arr)

    """
    print("Circle length: "+str(math.pi*4))
    angle = (1.00/(math.pi*4)*360)
    print("Angle: "+str(angle))
    print(turnRadius(1.00, 30.00))
    print(turnRadius(1.00, 13.76))
    print(turnRadius(1.00, 2.34))
    print(turnRadius(1.00, 90.00))
    print(turnRadius(2.45, 90.00))
    print("#############################")
    print(kochSnowflakeSq(243, 3))
    print(kochSnowflakeSq(19683, 7))
    print(kochSnowflakeSq(531441, 7))
    print(kochSnowflakeSq(531441, 9))
    """