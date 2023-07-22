# Bài 30: Cho số nguyên dương n. Kiểm tra xem n có phải là số hoàn thiện hay không

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=1
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print(n,'là số hoàn thiện')
else:
    print(n,'không là số hoàn thiện')