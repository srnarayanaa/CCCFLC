for t in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    #print(s)
    if n%2!=0:
        print(-1)
    else:
        xorp=[]
        for i in range(1,n):
            xorp.append(s[i]^s[0])
        #print(xorp)
        ans=[]
        for i in range(0,n-1):
            tmp=[]
            for j in range(0,n):
                tmp.append(xorp[i]^s[j])
            #print(tmp)
            if set(tmp)==set(s):
                ans.append(xorp[i])
        if len(ans)==0:
            print(-1)
        else:
            print(min(ans))
