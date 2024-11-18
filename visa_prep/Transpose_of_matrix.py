n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]
for row in transpose:
    print(*row)
