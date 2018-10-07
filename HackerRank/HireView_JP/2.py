def isPalindrome(number, count):
    
    if count == 0:
        return 0

    number = str(number)

    n = len(number)
    i = 0

    while i < n//2:

        if not number[i] == number[n-i-1]:
            return 0
        i+=1

    return 1



def reverseNumber(number):

    num_str = str(number)

    second_num_str = ""

    for char in reversed(num_str):
        second_num_str+=char

    second_num = int(second_num_str)
    return second_num



def palindromeCount(number):

    count = 0
    while not isPalindrome(number, count):
        
        second_num = reverseNumber(number)
        number = number+second_num
        count+=1


    return count, number



sol = palindromeCount(5)
print(sol)

# sol = reverseNumber(1215665)
# print(sol)

# sol = isPalindrome(123454321)
# print(sol)