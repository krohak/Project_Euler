# Given a staircase with N steps
# Can climb either one step, or two steps at a time
# Algo to count different ways the staircase can be climbed
# f( 1 ) -> 1
# f( 2 ) -> 2


def number_of_ways(N):
    
    # dp = [ 0  for _ in range(N+1) ]
    if N==1:
        return 1
    
    if N==2:
        return 2
    
    n_minus_2 = 1
    n_minus_1 = 2
    
    for _ in range(3, N+1):
        
        temp = n_minus_1
        n_minus_1 = n_minus_2+n_minus_1
        n_minus_2 = temp
    
    return n_minus_1


print(number_of_ways(1))
print(number_of_ways(2))
print(number_of_ways(3))
print(number_of_ways(4))

print(number_of_ways(100))

# f(n) = f(n-1) + f(n-2)