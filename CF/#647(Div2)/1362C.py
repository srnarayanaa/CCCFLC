for t in range(int(input())):
    n=int(input())
    bin_n=bin(n)[2:]
    ans=0
    l=len(bin_n)
    i=1
    ans=n-1
    while i<l:
        ans+=n//(2**i)
        i+=1
    print(ans+1)
