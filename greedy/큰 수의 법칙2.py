N,M,K = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
first = nums[N-1]
second = nums[N-2]
result = 0

count = int(M/(K+1))*K + M%(K+1)
result += count*first
result += (M-count)*second
print(result)