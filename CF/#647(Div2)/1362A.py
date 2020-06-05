for t in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    if a==b:
        print(0)
    else:
        if b>a:
            a,b=b,a
        ba=bin(a)[2:];lena=len(ba)
        bb=bin(b)[2:];lenb=len(bb)
        flag=1
        ind=ba.find(bb)
        if ind>0 or ind==-1:
            print(-1)
        else:
            res=ba[lenb:][::-1]
            while res!='':
                if res.find('000')==0:
                    ans+=1
                    res=res[3:]
                elif res.find('00')==0:
                    ans+=1
                    res=res[2:]
                elif res.find('0')==0:
                    ans+=1
                    res=res[1:]
                else:
                    flag=-1
                    break
            if flag==-1:
                print(-1)
            else:
                print(ans)
            
