# Bài 52: Tìm chữ số nhỏ nhất của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
temp=n
min=-1
while temp!=0:
    if min==-1 or min>temp%10:
        min=temp%10
    temp//=10

print('Chữ số nhỏ nhất của',n,'là',min)