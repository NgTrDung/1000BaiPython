# Bài 51: Tìm chữ số lớn nhất của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
temp=n
max=0
while temp!=0:
    if max<temp%10:
        max=temp%10
    temp//=10

print('Chữ số lớn nhất của',n,'là',max)