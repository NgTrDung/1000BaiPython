# Bài 105: Viết chương trình nhập 1 số nguyên có 2 chữ số. Hãy in ra cách đọc của số nguyên này

ones=['','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
tens=['','mười','hai mươi','ba mươi','bốn mươi','năm mươi','sáu mươi','bay mươi','tám mươi','chín mươi']

n=int(input('Nhập số nguyên có 2 chữ số: '))
numTens=int(n/10)
numOnes=int(n%10)

print(tens[numTens],ones[numOnes])
