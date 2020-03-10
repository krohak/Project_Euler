class Solution:
    def longestStrChain(self, words) -> int:

        wordSet = set(words)
        cache = {}

        def dp(string):
            if string in cache:
                return cache[string]

            res = 1
            for i in range(len(string)):
                excluded = string[0:i] + string[i + 1:]
                if excluded in wordSet:
                    res = max(res, dp(excluded) + 1)

            cache[string] = res
            return res

        for word in words:
            dp(word)

        return max(cache.values())