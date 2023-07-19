# Bài 13: Tính S(n) = x^2 + x^4 + … + x^2n

x=int(input('Nhập số nguyên dương x: '))
n=int(input('Nhập số nguyên dương n: '))
i=1
rst=0
while(i<=n):
    rst+=pow(x,2*i)
    i+=1

print('S(n) =',rst)