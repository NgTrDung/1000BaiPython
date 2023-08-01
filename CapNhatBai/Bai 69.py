# Bài 69: Tính S(x, n) = x – x^3 + x^5 + … + (-1)^n * x^2n+1

x,n=map(int,input('Nhập 2 số x,n: ').split())
i=0
sum=0
while i<=n:
    sum+=pow((-1),i)*pow(x,2*i+1)
    i+=1

print('S(x,n) =',sum)