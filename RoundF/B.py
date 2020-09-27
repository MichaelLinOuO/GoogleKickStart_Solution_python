import math
t=int(input())

for tt in range(t):

    N,K= map(int, input().split())
    a  =[]
    for _ in range(N):
        t1,t2 = map(int,input().split())
        a.append([t1,t2])
    a.sort()
    ans=0
    i=0

    #interval>k
    #[2,8] , interval 7
    #[2,5],[ 7,15]
    #[2,9],[9,
    curEnd=0
    while i<N:
        if curEnd>a[i][0]:
            curEnd = curEnd+K
        else:
            curEnd = a[i][0]+K

        ans += 1
        if a[i][1]>curEnd:
            need_interval= math.ceil((a[i][1]-curEnd)/K)
            curEnd = curEnd+ need_interval*K
            ans+=(need_interval)
            i+=1


        while i<N and a[i][1]<=curEnd:
            i+=1



    print("Case #{}: {}".format(tt + 1,ans))

