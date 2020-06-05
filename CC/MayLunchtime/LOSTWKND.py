for t in range(int(input())):
    arr=list(map(int,input().split()))
    if sum(arr[0:5])*arr[5]>120:
        print('Yes')
    else:
        print('No')
