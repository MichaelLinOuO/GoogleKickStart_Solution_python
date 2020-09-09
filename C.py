import heapq
def sol():
    n = int(input())

    q=[]
    er=[]
    sum=0
    for i in range(n):
        e,r = map(int,input().split())
        er.append([e,r])
        #minus-(e+r) beacuse of min heap.
        #when Ei+Ri>Esum->cry, put largest E+R at the beginning of q          
        heapq.heappush(q,[-(e+r),i])

        sum+= e
    tmp_sum = sum
    
    
    #if indefinite playing is possible, q has element left.
    while q:
        #largest passes->all passes
        if -q[0][0]<=tmp_sum:
            break
        else:
            tmp_sum -= er[q[0][1]][0]
            heapq.heappop(q)
    
    if q:
        print(n-len(q),"INDEFINITELY")
        return

    min_del=0
    mmax = sum
    total = sum
    ans_del=0
    for i in range(n):
        if er[i][0] + er[i][1] <=sum:
            total += er[i][0]
            heapq.heappush(q,[-(er[i][0]+er[i][1]),i])
            
            if total>mmax:
                mmax = total
                ans_del = min_del
        else:
            sum -= er[i][0]
            total-= er[i][0]
            min_del +=1
            while q and -q[0][0]> sum:
                tmp = heapq.heappop(q)
                index = tmp[1]
                #first cycle + second cycle
                total -= 2* er[index][0]
                sum -= er[index][0]
                min_del +=1
    print(ans_del,mmax)





t = int(input())
for tt in range(1,t+1):

    print("Case #{}: ".format(tt), end='')
    sol()