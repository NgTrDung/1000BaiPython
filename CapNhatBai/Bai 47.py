# Bài 47: Hãy tính tổng các chữ số chẵn của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
temp=n
sum=0
while temp!=0:
    if (temp%10)%2==0:
        sum+=temp%10
    temp//=10

print('S(n) =',sum)