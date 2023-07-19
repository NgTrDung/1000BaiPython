# Bài 11: Tính S(n) = 1 + 1.2 + 1.2.3 + … + 1.2.3….N

def GiaiThua(n):
    i=1
    rst=1
    while i<=n:
        rst*=i
        i+=1
    return rst

n=int(input('Nhập số nguyên dương n: '))
i=1
rst=1
while i<=n:
    rst*=GiaiThua(i)
    i+=1

print('S(n) =',rst)