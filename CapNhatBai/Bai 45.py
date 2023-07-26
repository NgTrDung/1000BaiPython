# Bài 45: Hãy tính tích các chữ số của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
rst=1
temp=n
while n!=0:
    numLast=n%10
    rst*=numLast
    n//=10

print('Tích các chữ số của',temp,'=',rst)