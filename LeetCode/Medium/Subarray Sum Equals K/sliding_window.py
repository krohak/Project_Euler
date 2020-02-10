arr = [1,2,3,4,5,6,7,8,9]


for window_size in range(0, len(arr)):
    for start in range(0, len(arr)-window_size):
        ans = []
        for i in range(start, start+window_size+1):
            ans.append(arr[i])
        print(ans,'\n')
    print('\n')


# for window_size in range(1, len(arr)+1):
#     for start in range(0, len(arr)+1-window_size):
#         ans = []
#         for i in range(start, start+window_size):
#             ans.append(arr[i])
#         print(ans,'\n')
#     print('\n')