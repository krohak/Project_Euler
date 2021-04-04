idi = 0
ratingi = 1
veganFriendlyi = 2
pricei = 3
distancei = 4

class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        
        sortedRestaurants  = sorted(restaurants, key=lambda rest: (rest[ratingi], rest[idi]), reverse=True)
        
        return [ rest[idi] for rest in sortedRestaurants if ( 
            (rest[veganFriendlyi] == veganFriendly if veganFriendly else 1) and 
            rest[pricei] <= maxPrice and 
            rest[distancei] <= maxDistance) 
       ]