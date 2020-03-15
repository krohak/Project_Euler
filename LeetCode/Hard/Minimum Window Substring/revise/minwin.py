super_string = "ADOBECODEBANC"
sub_string = "ABC"

super_string = "ZADOBECODEBANCX"
sub_string = "ZXO"


sub_set = set(sub_string)

sub_map = {}
for val in sub_set:
    sub_map[val] = -1


res_list = []

i = 0
window_start = 0
n = len(super_string)
while i < n:
    char = super_string[i]
    try:
        # try to access the char in hashmap
        last_position = sub_map[char]

        if not last_position == -1: # char previously found
            if last_position >= window_start: # repetition inside the window

                # save the current window config if not -1
                sub_map_values = list(sub_map.values())
                if not -1 in sub_map_values:
                    print('hello')
                    res_list.append(sub_map_values)

                # change window start (initialize new window)
                window_start = sub_map[char]

                # put current char position in window
                sub_map[char] = i

            elif last_position < window_start: # repetition in window

                # simply change the current char position in new window
                sub_map[char] = i
        
        else: # new char found
            # set the last position of new char
            sub_map[char] = i
    
    except Exception as e:
        # char not found in map (char not in sub_string)
        pass
    
    i+=1

res_list.append(list(sub_map.values()))

print(super_string)
print(sub_string)

res = res_list

sizes = [max(r)-min(r)+1 for r in res]
print(sizes)

min_size = min(sizes)


min_index, max_index = 0, 0
for i, size in enumerate(sizes):
    if size == min_size:
        min_index = min(res[i])
        max_index = max(res[i])
        break

print(min_index,max_index)

if min_index == -1 or max_index == -1:
    print('"')

else:
    print("{}".format(super_string[min_index:max_index+1]))