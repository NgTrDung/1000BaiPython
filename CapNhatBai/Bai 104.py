# Bài 104: Viết chương trình nhập ngày, tháng, năm. Tính xem ngày đó là ngày thứ bao nhiêu trong năm

d,m,y=map(int,input('Nhập ngày, tháng, năm: ').split())
sum=int(30.42*(m-1))+d
if m==2 or y%400==0 or y%4==0 and y%100!=0:
    sum+=1
if 2<m<8:
    sum-=1
print('Ngày thứ',sum,'trong năm')