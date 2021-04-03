class Solution:
    def findRestaurant(self, list1, list2):
        dict1 = { name: i for i, name in enumerate(list1) }
        dict2 = { name: i for i, name in enumerate(list2) }
        
        intersection = dict1.keys() & dict2.keys()
        
        dict3 = { name: dict1[name]+dict2[name] for name in intersection }
        
        dict3 = [ (name, rank) for name, rank in sorted(dict3.items(), key=lambda item: item[1])]
        
        highest_rank = dict3[0][1]
        
        common_interests = []
        for name, rank in dict3:
            if rank == highest_rank:
                common_interests.append(name)

        return common_interests