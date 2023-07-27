# Bài 49: Cho số nguyên dương n. Hãy tìm chữ số đầu tiên của n

n=int(input('Nhập số nguyên dương n: '))
temp=n
numFirst=0
while temp!=0:
    numFirst=temp%10
    temp//=10

print('Chữ số đầu tiên của',n,'là',numFirst)