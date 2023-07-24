# Bài 33: Tính S(n) = CanBac2(2+CanBac2(2+….+CanBac2(2 + CanBac2(2)))) có n dấu căn

import math

n=int(input('Nhập só nguyên dương n: '))
sum=0
i=1
while i<=n:
    sum+=math.sqrt(2+sum)
    i+=1

print('S(n) =',sum)