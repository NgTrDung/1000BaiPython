# Bài 53: Hãy đếm số lượng chữ số lớn nhất của số nguyên dương n

def MaxSo(n):
    temp=n
    max=0
    while temp!=0:
        if max<temp%10:
            max=temp%10
        temp//=10
    return max

n=int(input('Nhập số nguyên dương n: '))
temp=n
cnt=0
max=MaxSo(temp)
while temp!=0:
    if max==temp%10:
        cnt+=1
    temp//=10

print('Chữ số lớn nhất trong',n,'là',max,'với',cnt,'lần xuất hiện')
