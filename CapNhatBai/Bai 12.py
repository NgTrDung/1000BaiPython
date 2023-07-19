# Bài 12: Tính S(n) = x + x^2 + x^3 + … + x^n

x=int(input('Nhập số nguyên dương x: '))
n=int(input('Nhập số nguyên dương n: '))
i=1
rst=0
while(i<=n):
    rst+=pow(x,i)
    i+=1

print('S(n) =',rst)