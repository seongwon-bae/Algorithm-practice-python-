def go_left(x,y):
    x-=1
    if x<1:
        return (x+1),y
    else:
        return x,y
def go_right(x,y,size):
    x+=1
    if x>=size:
        return (x-1),y
    else:
        return x,y
def go_up(x,y):
    y-=1
    if y<1:
        return x,(y+1)
    else:
        return x,y
def go_down(x,y,size):
    y+=1
    if y>=size:
        return x,(y-1)
    else:
        return x,y

import sys, time
start = time.time()
size = int(sys.stdin.readline())
direction = map(str,sys.stdin.readline().split())
x,y = 1,1
for d in direction:
    if d=='L':
        x,y = go_left(x,y)
    elif d=='R':
        x,y = go_right(x,y,size)
    elif d=='D':
        x,y = go_down(x,y,size)
    else:
        x,y = go_up(x,y)
end = time.time()
print(y,x)
print('걸린 시간 : ',end-start)