# Bài 50: Hãy tìm số đảo ngược của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
temp=n
rst=0
while temp!=0:
    rst=rst*10+temp%10
    temp//=10

print('Chữ số đảo ngược của',n,'là',rst)