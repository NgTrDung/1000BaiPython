# Bài 48: Hãy tính tích các chữ số lẻ của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
rst=1
temp=n
while temp!=0:
    if (temp%10)%2!=0:
        rst*=temp%10
    temp//=10

print('Tích các chữ số lẻ của',n,'=',rst)