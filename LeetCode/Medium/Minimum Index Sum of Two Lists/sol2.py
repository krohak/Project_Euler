class Solution:
    def findRestaurant(self, list1, list2):
        dict1 = { name: i for i, name in enumerate(list1) }
        dict2 = { name: i for i, name in enumerate(list2) }
        
        intersection = dict1.keys() & dict2.keys()
        
        dict3 = [ [] for _ in range(len(list1)+len(list2)) ] 
        
        for name in intersection:
            rank = dict1[name]+dict2[name]
            dict3[rank].append(name)
        
        for l in dict3:
            if len(l):
                return l
            
        return []