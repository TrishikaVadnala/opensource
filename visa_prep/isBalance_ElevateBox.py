n = int(input())
A = list(map(int, input().split()))
B = []
for i in range(n):
    left_weight = sum(A[:i])
    right_weight = sum(A[i+1:])
    balance_value = abs(left_weight - right_weight)
    B.append(balance_value)
print(*B)
