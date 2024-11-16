X,Y,Z=map(int,input().split())
tc=X+Y
tt=Z*24*60
if tc <= tt:
    print("YES")
else:
    print("NO")
