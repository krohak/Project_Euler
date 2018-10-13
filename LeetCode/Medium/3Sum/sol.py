
# a+b+c = 0 ?


def threeSUM(arr):

    pos_map = {}

    for elem in arr:
        if elem not in pos_map:
            pos_map[elem] = 1
        else:
            pos_map[elem]+=1

    sol = []

    n = len(arr)
    i = 0

    while i<n:
        j = i+1
        while j<n:

            pos_map[arr[i]]-=1
            pos_map[arr[j]]-=1
            remaining = -(arr[i] + arr[j])

            if remaining in pos_map:
                if pos_map[remaining] > 0:
                    sol.append([arr[i],arr[j],remaining])
            
            pos_map[arr[i]]+=1
            pos_map[arr[j]]+=1

            j+=1
        i+=1

    return sol


arr = [-1,0,1,2,-1,-4]
sol = threeSUM(arr)
print(sol)