class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        if not s: return 0
        if k>len(s): return 0
        left, right = 0, 0
        counter = {} 
        answer = 0
        while left < len(s):
            while right - left < k:
                if s[right] not in counter:
                    counter[s[right]] = right
                    right+=1
                else: break

            if right - left == k: answer+=1

            if s[right] in counter:
                rightRemove = counter[s[right]]
                while left<=rightRemove:
                    del counter[s[left]]
                    left+=1
                counter[s[right]] = right
                right+=1

            if right - left >= k:
                del counter[s[left]]
                left+=1
                
        return answer


print(Solution().numKLenSubstrNoRepeats("havefunonleetcode", 5))