import sys
n,m = map(int,sys.stdin.readline().split())
a,b,direction = map(int,sys.stdin.readline().split())
d = [[0] * m for _ in range(n)]
d[a][b] = 1
game_map = []
for i in range(n):
    game_map.append(list(map(int,sys.stdin.readline().split())))

# x,y가 는 각각 이동할 값
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
count = 1
turn_time = 0
while 1:
    turn_left()
    next_x = a+dx[direction]
    next_y = b+dy[direction]
    if game_map[next_x][next_y] == 0 and d[next_x][next_y] == 0:
        d[next_x][next_y] = 1
        a = next_x
        b = next_y
        count += 1
        turn_time=0
        continue
    else:
        turn_time += 1
    if turn_time==4:
        next_x = a-dx[direction]
        next_y = b-dy[direction]
        if game_map[next_x][next_y] == 0:
            a = next_x
            b = next_y
        else:
            break
        turn_time=0
print(count)

