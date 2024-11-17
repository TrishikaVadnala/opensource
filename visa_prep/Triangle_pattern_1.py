N = int(input())
current_number = 1
for row in range(1, N + 1):
    for _ in range(row):
        print(current_number, end=" ")
        current_number += 1
    print()
