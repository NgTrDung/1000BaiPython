# Bài 14: Tính S(n) = x + x^3 + x^5 + … + x^2n + 1

x=int(input('Nhập số nguyên dương x: '))
n=int(input('Nhập số nguyên dương n: '))

i=0
rst=0
while(i<=n):
    rst+=pow(x,2*i+1)
    i+=1

print('S(n) =',rst)