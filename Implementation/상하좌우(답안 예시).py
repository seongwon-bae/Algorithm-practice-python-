import time
start2 = time.time()
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for p in plans:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny
end2 = time.time()
print(x,y)
print('걸린 시간 : ',end2-start2)