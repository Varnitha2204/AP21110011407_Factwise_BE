list1 = list(map(int,input().split()))
n = len(list1)
x,y = [],[]
k = int(input())
c1,c2 = 0,0
if(k!=len(list1)):
    for i in range(k):
        x.append(list1[i])
        y.append(list1[n-i-1])
    sx = sum(x)
    sy = sum(y)
    for i in range(k):
        if(max(x)<=y[i]):
            c1+=1
        if(max(y)<=x[i]):
            c2+=1
    if(c1==k or c1>=1):
        print(sum(y))

    elif(c2==k or c2>=1):
        print(sum(x))
    
else:
    print(sum(list1))

