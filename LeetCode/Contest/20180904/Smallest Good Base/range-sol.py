from math import log, ceil

number = int(input())

# number = 2251799813685247
# digits = ceil(log(number, 2))
# print(digits)

for base in range(2, number+1):
    # print(base)
    # print(base)
    digits = ceil(log(number, base))

    dig_sum = 0
    base_add = base
    
    dig_sum = ((base**digits ) -1) // (base-1)
    print(digits, base, dig_sum, digits) 
    # for _ in range(digits):
    #     dig_sum += base_add
    #     base_add *= base

    if dig_sum == number:
        print(base)
        break