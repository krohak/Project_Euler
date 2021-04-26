restaurants = [
    "WalBuers",
    "Buer Kin",
    "MallBuers",
    "DDI",
    "Bob's Buers",
    "DDI Diner",
    "Suppet Buers",
    "Inut Buers"
]

def getKrestaurants(keyword, k):
    """
    full text matches, prefix matches

    input=Buer, restaurant=WahlBuers
    full text match

    input=Buer, restaurant=Buer King
    prefix match

    5 prefix matches, 3 full text matches, k = 6
    [5 prefix matches, 1 full text match]
    """
    
    searchResults = []
    counter = 0
    prefixDone = set()
    
    for restaurant in restaurants:
        restaurantList = restaurant.split(' ')
        for i in range(len(restaurantList)):
            if (' '.join(restaurantList[i:]).lower()).startswith(keyword):
                searchResults.append(restaurant)
                prefixDone.add(restaurant)
                counter+=1
                break
        if counter==k:
            return searchResults
            
    for restaurant in restaurants:
        if keyword in restaurant and restaurant not in prefixDone:
            searchResults.append(restaurant)
            counter+=1
        if counter==k:
            return searchResults
                 
    return searchResults

    
        
print(getKrestaurants('bur',4))
print(getKrestaurants('bur',5))
print(getKrestaurants('bur',6))
# print(getKrestaurants('bur',3))
# print(getKrestaurants('Buers',3))
# print(getKrestaurants('Buer k',2))

# n -> avg num of character in each restaurant
# y -> avg num of words in restaurant
# x -> avg num of characters in each keyword

# nxy
# n(x^2)
 
# Input:  "Buers", k=4 
# Output: ["Bob’s Buers", "Suppet Buers", "In-n-Out Buers"]

# Input:  "Buers", k=2
# Output: ["Bob’s Buers", "Suppet Buers"]