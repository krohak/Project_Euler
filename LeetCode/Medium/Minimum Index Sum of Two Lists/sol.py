class Solution:
    def findRestaurant(self, list1 , list2 ):
        dict1 = { name: i for i, name in enumerate(list1) }
        dict2 = { name: i for i, name in enumerate(list2) }
        
        intersection = dict1.keys() & dict2.keys()
        
        lowest_rank = float('inf')
        lowest_list = []
        
        for name in intersection:
            rank = dict1[name]+dict2[name]
            if rank < lowest_rank:
                lowest_rank = rank
                lowest_list = [name]
            elif rank == lowest_rank:
                lowest_list.append(name)
            
        return lowest_list