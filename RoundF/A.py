t=int(input())

for tt in range(t):

    people, X = map(int, input().split())
    a = list(map(int, input().split()))
    indexlist =[]
    for i in range(people):
        indexlist.append([a[i],i])
    res = []

    while indexlist:
        cur = indexlist[0][0] - X
        if cur > 0:
            indexlist.append([cur,indexlist[0][1]])
            indexlist.pop(0)
        else:

            res.append(indexlist[0][1]+1)
            indexlist.pop(0)

    print("Case #{}: ".format(tt + 1),end='')
    print(*res)

