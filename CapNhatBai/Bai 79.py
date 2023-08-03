# Bài 79: Hãy đếm số lượng chữ số của số nguyên dương n

n=int(input('Nhap so nguyen duong n: '))
cnt=0
temp=n
while temp>0:
    cnt+=1
    temp//=10

print(n,'co',cnt,'chu so')