T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    runs_needed = x - y + 1
    print(runs_needed)
