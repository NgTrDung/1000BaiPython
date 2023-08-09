# Bài 98: Lập chương trình giải hệ: ax + by = c
# Dx + ey = f. Các hệ số nhập từ bàn phím

a,b,c,d,e,f=map(float,input('Nhập các hệ số: ').split())
delta=a*e-b*d
if delta==0:
    print('Phương trình vô nghiệm')
else:
    x=(c*e-b*f)/delta
    y=(a*f-c*d)/delta
    print('Nghiệm của hệ phương trình là:')
    print('x =',round(x,2))
    print('y =',round(y,2))