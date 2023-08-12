# Bài 106 Viết chương trình nhập 1 số nguyên có 3 chữ số. Hãy in ra cách đọc của số nguyên này

n=int(input('Nhập số nguyên có 3 chữ số: '))

ones=['','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
tens=['linh','mười','hai mươi','ba mươi','bốn mươi','năm mươi','sáu mươi','bay mươi','tám mươi','chín mươi']
hunds=['','một trăm','hai trăm','ba trăm','bốn trăm','năm trăm','sáu trăm','bảy trăm','tám trăm','chín trăm']

numOnes=int(n%10)
numTens=int((n/10)%10)
numHunds=int(n/100)

if n==100:
    print('một trăm')
else:
    print(hunds[numHunds],tens[numTens],ones[numOnes])