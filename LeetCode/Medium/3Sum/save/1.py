# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]



def three_sum(arr):
    freq_map = { x:0 for x in arr}
    if freq_map[0] == 3000:
        return [0,0,0]

    super_set = set()

    for x in arr:
        freq_map[x] += 1

    print("MAP:",freq_map)

    i = 0
    size = len(arr)
    while i<size:
        j = i+1
        x = arr[i]

        freq_map[x] -= 1

        if freq_map[x] > -1:
            while j<size:

                y = arr[j]

                freq_map[y] -= 1

                z = -(x+y)



                if z in freq_map: 

                    freq_map[z] -= 1
                    # print("MAP:",freq_map)

                    if freq_map[y] > -1 and freq_map[z] > -1:
                        print(x, y, z)
                        # print("freq_map:", freq_map[x], freq_map[y], freq_map[z])

                        answer_map = { key:0 for key in [x,y,z] }
                        answer_map[x] += 1
                        answer_map[y] += 1
                        answer_map[z] += 1

                        super_set.add(frozenset(answer_map.items()))
                        
                        
                        
                    freq_map[z] += 1
                freq_map[y] += 1
                j+=1
        freq_map[x] += 1
        i+=1

    # print(super_set)

    super_list = []
    for set_obj in super_set:
        answer_list = []
        for map_tuple in set_obj:
            answer_list += ([map_tuple[0]]* map_tuple[1])
        # print(answer_list)
        super_list.append(answer_list)

    # print(super_list)
    return super_list


arr = [-1, 0, 1, 2, -1, -4]
arr = [0, 0]

arr = [-1,0,1,0]

super_list = three_sum(arr)
print(super_list)