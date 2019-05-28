# 1. line 불러오기
with open('number.txt', 'r') as f :
    lines = f.readlines()
    print(lines)
# 2. 뒤집기
lines.reverse()
print(lines)
# 3. 다시 작성하기
with open('number.txt', 'w') as f :
    for line in lines :
        f.write(line)

#
# for line in lines[::-1] :
#     print(line)