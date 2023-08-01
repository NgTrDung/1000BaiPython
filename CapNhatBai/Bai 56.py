# Bài 56: Hãy kiểm tra số nguyên dương n có toàn chữ số lẻ hay không

n=int(input('Nhập số nguyên dương n: '))
temp=n
flag=1
while temp!=0:
    if (temp%10)%2==0:
        flag=0
        break
    temp//=10
print(n, 'gồm toàn chữ số lẻ') if flag == 1 else print(n, 'có chữ số chẵn')
