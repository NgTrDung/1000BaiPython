# Bài 59: Hãy kiểm tra số nguyên dương n có phải là số đối xứng hay không

n=int(input('Nhập số nguyên dương n: '))
temp=n
sum=0
while temp!=0:
    sum=sum*10+(temp%10)
    temp//=10

print(n,'là số đối xứng') if n==sum else print(n,'không là số đối xứng')