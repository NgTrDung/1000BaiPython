# Bài 86: Tính S(n) = 1^3 + 2^3 + … + N^3

n=int(input('Nhập số nguyên dương n: '))
sum=0
for i in range(n+1):
    sum+=pow(i,3)

print(sum)