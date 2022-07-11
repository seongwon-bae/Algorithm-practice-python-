N,M,K = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
first = nums[N-1]
second = nums[N-2]
result = 0
while 1:
    for i in range(K):
        if M==0:
            break
        result += first
        M-=1
    if M==0:
        break
    result += second
    M-=1
print(result)