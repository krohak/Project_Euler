def pal(n):
    flag=1
    for i in range(int(len(n)/2)):
        if n[i]!=n[len(n)-i-1]:
            flag=0
    return flag




def check():
    prev=0
    for x in (range(100,1000)):
        for y in (range(100,1000)):
            #print(x,y)
            ans=pal(str(x*y))
            if ans==1 and x*y>prev:
                #print(x*y)
                prev=x*y
    return prev




print(check())

#print(pal("99099"))
#print(len("9009"))
