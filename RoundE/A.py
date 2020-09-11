t = int(input())
for tt in range(t):
    n=int(input())
    a= list(map(int,input().split()))

    ans=0
    i=1
    while i<n:
        cur = a[i]-a[i-1]
        cnt=2
        i+=1

        for y in range(i,n):
            if a[y]-a[y-1] == cur:
                cnt+=1
            else:
                ans = max(ans,cnt)
                i=y
                break
            if y==n-1:
                i=n

    ans=max(ans,cnt)

    print("Case #{}: {}".format(tt+1, ans))