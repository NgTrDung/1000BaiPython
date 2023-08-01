# Bài 68: Tính S(x, n) = -x^2 + x^4 + … + (-1)^n * x^2n

x,n=map(int,input('Nhập 2 số x,n: ').split())
i=1
sum=0
while i<=n:
    sum+=pow((-1),i)*pow(x,2*i)
    i+=1

print('S(x,n) =',sum)