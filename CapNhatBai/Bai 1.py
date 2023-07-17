'''Bài 1: Tính S(n) = 1 + 2 + 3 + … + n'''

n=int(input('Nhập số nguyên dương n: '))
sum=0
for i in range(1,n+1):
    sum+=i

print('S(n) = {0}'.format(sum))
