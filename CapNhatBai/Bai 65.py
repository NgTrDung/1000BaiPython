#Bài 65: Giải pt bậc 2

import math

a,b,c=map(int,input('Nhập 3 số a, b, c: ').split())
delta=pow(b,2)-4*a*c
if delta<0:
    print('Pt vô nghiệm')
elif delta==0:
    print('x1 = x2 =',-b/(2*a))
else:
    print('x1 =',((-b+math.sqrt(delta))/(2*a)))
    print('x2 =',((-b-math.sqrt(delta))/(2*a)))