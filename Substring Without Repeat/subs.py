def get_longest_substring(string):
    # to store the last seen position of a character in the given string
    hashmap={}
    # window start at
    i = 0
    # window end at
    j = 0
    result = 0
    final_result = 0
    while j < (len(string)):
        if string[j] not in hashmap:
            hashmap[string[j]] = j
            # increase window size
            j+=1
            result+=1
        # if char already in hashmap
        else:
            # if char at start of window
            if hashmap.get(string[j]) == i:
                # update char position with latest
                hashmap[string[j]] = j
                j+=1
                #increment window start at
                i+=1
            # if char not at start window, give up on this substring.
            else:
                # check if longest, update
                if result>final_result:
                    final_result = result
                # start window from the previous occurance of char+1
                i = j = hashmap[string[j]]+1
                # flush hashmap
                hashmap={}
                result = 0
    if result>final_result:
        return result
    return final_result

string = "ohvhjdml"
print(get_longest_substring(string))
