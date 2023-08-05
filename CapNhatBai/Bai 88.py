# Bài 88: Hãy sử dụng vòng lặp for để xuất tất cả các ký tự từ A đến Z

for char_code in range(ord('A'), ord('Z')+1):
    char = chr(char_code)
    print(char, end=' ')
