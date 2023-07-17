'''Bài 2: Tính S(n) = 1^2 + 2^2 + … + n^2'''

n=int(input('Nhập số nguyên dương n: '))
sum=0
for i in range(1,n+1):
    sum+=pow(i,2)

print('S(n) = ',sum)
