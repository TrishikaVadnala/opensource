N = int(input())
attendance = list(map(int, input().split()))
max_consecutive_absents = 0
current_absents = 0
for day in attendance:
    if day == 0:
        current_absents += 1
        max_consecutive_absents = max(max_consecutive_absents, current_absents)
    else:
        current_absents = 0
print(max_consecutive_absents)
