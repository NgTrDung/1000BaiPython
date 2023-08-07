# Bài 90: Viết chương trình tìm số nguyên dương m lớn nhất sao cho 1 + 2 + … + m < N

N=int(input("Nhập số nguyên dương N: "))
sum=0
i=1
while sum+i<N:
    sum+=i
    i+=1

print('Số nguyên dương m lớn nhất =',i-1)

