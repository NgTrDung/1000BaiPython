# Bài 44: Hãy tính tổng các chữ số của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
sum=0
temp=n
while n!=0:
    numLast=n%10
    sum+=numLast
    n//=10

print('Tổng các chữ số của',temp,"=",sum)