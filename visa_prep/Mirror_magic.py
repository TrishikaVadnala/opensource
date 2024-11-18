n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
mirror_image = [row[::-1] for row in matrix]
for row in mirror_image:
    print(*row)
