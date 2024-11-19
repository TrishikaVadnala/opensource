N = int(input())
arr = list(map(int, input().split()))
single_number = 0
for num in arr:
    single_number ^= num
print(single_number)
