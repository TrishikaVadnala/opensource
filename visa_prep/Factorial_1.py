def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input())
if 1<=n<=15:
    print(factorial(n))
else:
    print("Input out of range")
