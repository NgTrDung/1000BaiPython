# Bài 102: Viết chương trình nhập vào 1 ngày (ngày, tháng, năm). Tìm ngày kế ngày vừa nhập (ngày, tháng, năm)
# Bài 103: Viết chương trình nhập vào 1 ngày ( ngày, tháng, năm). Tìm ngày trước ngày vừa nhập (ngày, tháng, năm)

def DayInMonth(m,y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    else:
        if y%400==0 or y%4==0 and y%100!=0:
            return 29
        else:
            return 28
        
d,m,y=map(int,input('Nhập ngày, tháng, năm: ').split())
d=(d%(DayInMonth(m,y)))+1
if d==1:
    m=(m%12)+1
print('Ngày mai: {:02}/{:02}/{:02}'.format(d,m,y))

d,m,y=map(int,input('Nhập ngày, tháng, năm: ').split())
if d==1:
    if m==1:
        m=12
        y-=1
    else:
        m-=1
    d=DayInMonth(m,y)
else:
    d-=1
print('Ngày hôm qua: {:02}/{:02}/{:02}'.format(d,m,y))