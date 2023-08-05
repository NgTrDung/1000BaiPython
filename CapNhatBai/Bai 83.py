# Bài 83: Viết chương trình nhập 2 số thực, kiểm tra xem chúng có cùng dấu hay không
a,b=map(float,input('Nhap 2 so thuc a,b: ').split())
print('2 so a,b cung dau') if a*b>0 else print('2 so a,b trai dau')