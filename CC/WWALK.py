for t in range(int(input())):
    N=int(input())
    alice=list(map(int,input().split()))
    bob=list(map(int,input().split()))
    a=0
    b=0
    ans=0
    for i in range(N):
        if a==b and alice[i]==bob[i]:
            ans+=alice[i]
        else:
            a+=alice[i]
            b+=bob[i]
    print(ans)
