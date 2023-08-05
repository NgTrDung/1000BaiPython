# Bài 82: Viết chương trình tìm số lớn nhất trong 3 số thực a, b, c

a,b,c=map(float,input('Nhap 3 so thuc a, b, c: ').split())
print('so lon nhat trong 3 so la',max(a,max(b,c)))