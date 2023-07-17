'''Bài 5: Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)'''

n=int(input('Nhập số nguyên dương n: '))
sum=1
i=1
while(i<=n):
    sum+=1/(2*i+1)
    i+=1

print('S(n) = ',sum)