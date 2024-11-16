v,t = map(str,input().split())
if (v=='R' and t=='S') or (v=='S' and t=='P') or (v=='P' and t=='R'):
    print("Vignesh")
elif (t=='R' and v=='S') or (t=='S' and v=='P') or (t=='P' and v=='R'):
    print("Charan")
else:
    print("NULL")
