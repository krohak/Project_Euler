class Solution(object):
    def threeSum(self,arr):

        arr.sort()

        pos_map = {}

        for elem in arr:
            if elem not in pos_map:
                pos_map[elem] = 1
            else:
                pos_map[elem]+=1
        
        sol = []

        n = len(arr)
        i = 0

        for i in range(n):

            if i>0:
                if arr[i] == arr[i-1]:
                    continue

            for j in range(i+1,n):

                if j>i+1:
                    if arr[j] == arr[j-1]:
                        continue

                pos_map[arr[i]]-=1
                pos_map[arr[j]]-=1
                remaining = -(arr[i] + arr[j])

                if remaining in pos_map:
                    if pos_map[remaining] > 0 and remaining > arr[i] and remaining > arr[j]:
                        sol.append([arr[i],arr[j],remaining])
                
                pos_map[arr[i]]+=1
                pos_map[arr[j]]+=1

        return sol


nums = [-1,0,1,2,-1,-4]
sol = Solution().threeSum(nums)
print(sol)