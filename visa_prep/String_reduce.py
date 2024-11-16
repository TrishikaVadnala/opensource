def reduce_string(s):
    result = ""
    count = 1
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i -1]:
            count += 1
        else:
            result += s[i -1] +str(count)
            count = 1
    result += s[-1] + str(count)
    return result
s=input()
print(reduce_string(s))
