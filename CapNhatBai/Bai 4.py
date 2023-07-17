'''Bài 4: Tính S(n) = ½ + ¼ + … + 1/2n'''

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=1
while(i<=n):
    sum+=1/(2*i)
    i+=1

print('S(n) = ',sum)