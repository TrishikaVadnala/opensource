N = int(input())
for i in range(1, N + 1):
    left_triangle = "".join(str(x) for x in range(1, i + 1))
    right_triangle = "".join(str(x) for x in range(i, 0, -1))
    spaces = " " * (2 * (N - i))
    print(left_triangle + spaces + right_triangle)
