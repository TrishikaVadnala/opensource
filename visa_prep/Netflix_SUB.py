A,B,C,x= map(int, input().split())
if(A+B>=x):
    print("YES")
elif(B+C>=x):
    print("YES")
elif(C+A>=x):
    print("YES")
else:
    print("NO")
