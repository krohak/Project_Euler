# Given a string input S, which is periodic, write a function that identifies the period and
# the repeating string 
# abcabcabc -> P=abc, n=3
# xxxxxxxxx -> P=x, n=9 S = P times n
# qwerqwer -> P=qwer, n=2
# S -> P, n
# abcabcab -> P=abcabcab, n=1


def is_periodic(string):
    
    for window_size in range(1, len(string)):
        current_window = string[:window_size]
        is_priodic_window = True
        for iteration in range(window_size, len(string), window_size):
            if not current_window == string[iteration:iteration+window_size]:
                is_priodic_window = False
                break
            
        if is_priodic_window:
            return current_window, len(string) // window_size
    
    return string, 1
            

window, size = is_periodic("abcabc")
print(window, size)


window, size = is_periodic("abcabca")
print(window, size)

window, size = is_periodic("xxxx")
print(window, size)

# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()
