# Bài 36: Tính S(n) = CanBac2(n! + CanBac2((n-1)! +CanBac2((n – 2)! + … + CanBac2(2!) + CanBac2(1!)))) có n dấu căn

import math

def GiaiThua(n):
    rst=1
    i=1
    while i<=n:
        rst*=i
        i+=1
    return rst

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=0
while i<=n:
    sum+=math.sqrt((GiaiThua(i+1))+sum)
    i+=1

print('S(n) =',sum)