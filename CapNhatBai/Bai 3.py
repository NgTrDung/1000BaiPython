'''Bài 3: Tính S(n) = 1 + ½ + 1/3 + … + 1/n'''

n=int(input('Nhập số nguyên duong n: '))
sum=0
i=1
while (i<=n):
    sum+=1/i
    i+=1

print('S(n) = ',sum)