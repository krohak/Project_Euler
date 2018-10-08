# http://www.cnblogs.com/grandyang/p/5006441.html
# https://blogs.technet.microsoft.com/galstertechblog/2016/03/31/burst-balloons/

def burstBalloons(balloons):

    n = len(balloons)

    balloons.append(1)
    balloons.insert(0,1)

    L = {}

    i = 0
    while i<len(balloons):
        j=0
        while j<len(balloons):
            L[(i,j)] = 0
            j+=1
        i+=1

    win_size = 1
    while win_size <=n:

        win_start = 1

        while win_start <= n - win_size + 1:
            
            pointer = win_start
            win_end = win_start+win_size-1
            while pointer <= win_end:
                
                # print(pointer+1,win_end)

                L[(win_start,win_end)] = max( 
                    L[(win_start,win_end)], 
                    balloons[win_start-1]
                    *balloons[pointer]
                    *balloons[win_end+1]
                    +L[(win_start,pointer-1)]
                    +L[(pointer+1,win_end)]
                )

                pointer+=1
            
            win_start+=1

        win_size+=1

    return L[1,n]


sol = burstBalloons([3,1,5,8])
print(sol)