# Bài 17: Tính S(n) = x + x^2/2! + x^3/3! + … + x^n/N!

def GiaiThua(n):
    rst=1
    i=1
    while(i<=n):
        rst*=i
        i+=1
    return rst

x,n=map(int,input('Nhập số nguyên dương x, n: ').split())
rst=0
i=1
while(i<=n):
    rst+=(pow(x,i))/GiaiThua(i)
    i+=1

print('S(n) =',rst)