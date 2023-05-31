import math

n = int(input())

lucky = [4, 7, 47, 74, 774, 477, 474, 447]

almost_lucky= False

for i in lucky:
    if n % i == 0:
        almost_lucky = True  
        break 


if almost_lucky:
    print("YES")
else:
    print("NO")