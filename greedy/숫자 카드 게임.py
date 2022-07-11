n,m = map(int,input().split())
maximum = 0
for _ in range(n):
    numbers = list(map(int,input().split()))
    numbers.sort()
    if maximum < numbers[0]:
        maximum = numbers[0]
print(maximum)