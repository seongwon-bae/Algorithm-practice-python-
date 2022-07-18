import sys
location = sys.stdin.readline()
row = int(location[1])
# 'ord'함수로 아스키코드 확인
col = int(ord(location[0])) - int(ord('a'))+1
steps = [(-2,1), (-2,-1), (2,-1), (2,1), (1,-2), (-1,-2), (1,2), (-1,2)]
result = 0
for s in steps:
    next_row = row + s[0]
    next_col = col + s[1]
    if next_row>=1 and next_row <=8 and next_col>=1 and next_col<=8:
        result += 1
print(result)