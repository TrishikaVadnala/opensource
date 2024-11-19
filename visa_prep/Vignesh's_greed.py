N = int(input())
stricks = list(map(int, input().split()))
stricks.sort(reverse=True)
for i in range(N - 2):
    if stricks[i] < stricks[i + 1] + stricks[i + 2]:
        print(stricks[i] + stricks[i + 1] + stricks[i + 2])
        break
else:
    print(-1)
