# Bài 34: Tính S(n) = CanBac2(n+CanBac2(n – 1 + CanBac2( n – 2 + … + CanBac2(2 + CanBac2(1) có n dấu căn

import math

n=int(input('Nhập số nguyên dương n: '))

sum=0
i=0
while i<=n:
    sum+=math.sqrt((i+1)+sum)
    i+=1

print('S(n) =',sum)
