# Bài 89: Viết chương trình tính tổng các giá trị lẻ nguyên dương nhỏ hơn N

n=int(input('Nhập số nguyên dương n: '))
sum=0
for i in range(n):
    if i>0 and i%2!=0:
        sum+=i

print(sum)