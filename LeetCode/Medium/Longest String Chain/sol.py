class Solution:
    def longestStrChain(self, words) -> int:

        dp = {}

        words.sort(key=lambda x: len(x))

        for word in words:

            running_max = 0
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]

                if new_word in dp:
                    running_max = max(running_max, dp[new_word])

            dp[word] = running_max+1

        return max(dp.values())