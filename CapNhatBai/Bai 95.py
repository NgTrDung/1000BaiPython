# Bài 95: Viết chương trình nhập 3 số thực. Hãy thay tất cả các số âm bằng trị tuyệt đối của nó

import math

a,b,c=map(float,input('Nhập 3 số thực a,b,c: ').split())
if a<0:
    a=abs(a)
if b<0:
    b=abs(b)
if c<0:
    c=abs(c)

print(a,b,c)