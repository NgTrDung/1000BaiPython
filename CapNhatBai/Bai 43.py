# Bài 43: Hãy đếm số lượng chữ số của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
cnt=0
temp=n
while n!=0:
    n//=10
    cnt+=1

print(temp,'có',cnt,'chữ số')