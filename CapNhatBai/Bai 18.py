# Bài 18: Tính S(n) = 1 + x^2/2! + x^4/4! + … + x^2n/(2n)!

def GiaiThua(n):
    rst=1
    i=1
    while(i<=2*n):
        rst*=i
        i+=1
    return rst

x,n=map(int,input('Nhập số nguyên dương x, n: ').split())
rst=1
i=1
while(i<=n):
    rst+=(pow(x,2*i))/GiaiThua(i)
    i+=1

print('S(n) =',rst)