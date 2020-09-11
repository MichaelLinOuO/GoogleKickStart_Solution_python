t = int(input())
for tt in range(t):
    N,A,B,C=map(int,input().split())

    a=[]
    if N == 2:
        insertwt = 1
    else:
        insertwt = 2
    for i in range(C):
        a.append(N)
    if N>1 and A==1 and B==1 and C==1:
        print("Case #{}: ".format(tt + 1), end='')
        print("IMPOSSIBLE")
        continue
    elif A==B and B==C:
        total = N-C
        for e in range(total):
            a.insert(1,1)
    else:
        insertside=0
        if A<B:
            use=A
            remain=B
        else:
            #1=right
            insertside=1
            use=B
            remain=A

        more = use-C

        if more>=0:
            for i in range(more):
                if insertside:
                    a.append(1)
                else:
                    a.insert(0,1)

        remain = remain-C
        totalremain = N -remain - more - C
        if totalremain<0:
            print("Case #{}: ".format(tt+1),end='')
            print("IMPOSSIBLE")
            continue

        for e in range(totalremain):
            if insertside:
                a.insert(0, 1)
            else:
                a.append(1)
        if remain:
            for i in range(remain):

                if insertside:
                    a.insert(0,insertwt)
                else:
                    a.append(insertwt)

    print("Case #{}: ".format(tt+1),end='')
    print(*a)