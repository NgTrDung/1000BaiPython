# Bài 46: Hãy đếm số lượng chữ số lẻ của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
cnt=0
temp=n
while temp!=0:
    if (temp%10)%2!=0:
        cnt+=1
    temp//=10

print(n,'có',cnt,'chữ số lẻ')