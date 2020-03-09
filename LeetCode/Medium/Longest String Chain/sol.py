# Given a list of words, each word consists of English lowercase letters.

# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

# Return the longest possible length of a word chain with words chosen from the given list of words.



# Example 1:

# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
  

#       a,b,ba,bca,bda
# dp = [0,0,0,x,y, max(x,y)+1]
 
# set(a,b,ba,bca,bda)

# hashmap (a) = 0
  
# curr_elem = bdca  
  
#   dca
#   bca
#   bda
#   dca
  
#   bdca
  
#   bca   bda
        
#         ba
#   b a    
      
#        b a
        
# NlogN

# N*S*S

# S**2 > logN

# O(N*S**2 + NlogN)


def longestStrChain(words) -> int:
  
  n = len(words)
  
  dp = {}
  
  words.sort()
  
  for word in words:
    
    running_max = 0
    for i in range(len(word)):
      new_word = word[:i] + word[i+1:]
      
      if new_word in dp:
        running_max = max(running_max, dp[new_word])
     
    dp[word] = running_max+1
   
  
  max_in_hash = 0
  for key, val in dp:
    max_in_hash = max(max_in_hash, val)
    
   
  return max_in_hash
      
    
   
# ["a","b","ba","bca","bda","bdca"]
  
# n = 6
# dp = {}


# 1
# word = a
# running_max = 0

# dp = {a:1}

# 2
# dp = {a:1,b:1}


# 3

# word = ba

# b, a
# running_max = 1


# dp = {a:1, b:1, ba:2}

# 4
# bca

# bc
# ba
# ca

# running_max = 2

# dp = {a:1, b:1, ba:2, bca:3}

# 5
# bda

# dp = {a:1, b:1, ba:2, bca:3, bda:3}
      

# 6

# word = bdca


# bdc
# bca : 3
# bda : 3
# bdc

# running_max = 3
# dp = {a:1, b:1, ba:2, bca:3, bda:3, bdca:4}

# 4

# bca ->
# |   |
# bc   ba
# | |  | |
# b c  b a

# b : 1
# c : 1
  
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



# https://leetcode.com/problems/longest-string-chain