from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        dic = defaultdict(list)        
        for st in strs:
            dic[frozenset(Counter(st).items())].append(st)        
        return dic.values()