# Bài 15: Tính S(n) = 1 + 1/1 + 2 + 1/ 1 + 2 + 3 + ….. + 1/ 1 + 2 + 3 + …. + N

def TongMau(n):
    i=1
    rst=0
    while(i<=n):
        rst+=i
        i+=1
    return rst

n=int(input('Nhập số nguyên dương n: '))

i=1
rst=0
while(i<=n):
    rst+=1.0/TongMau(i)
    i+=1

print('S(n) =',rst)