class Solution(object):
    def findRestaurant(self, list1, list2):
        restaurants, leastSum = [], float('inf')
        list1Name2Index = { name: i for i,name in enumerate(list1) }
        for j, name in enumerate(list2):
            i = list1Name2Index.get(name, float('inf'))
            if i+j < leastSum:
                leastSum = i+j
                restaurants = [name]
            elif i+j == leastSum:
                restaurants.append(name)
        return restaurants