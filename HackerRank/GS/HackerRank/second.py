
alphabet = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
,'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


alphabet_set = set(alphabet)


alphabet_dict = {
'b':'B',
'c':'C',
'd':'D',
'e':'E',
'f':'F',
'g':'G',
'h':'H',
'i':'I',
'j':'J',
'k':'K',
'l':'L',
'm':'M',
'n':'N',
'o':'O',
'p':'P',
'q':'Q',
'r':'R',
's':'S',
't':'T',
'u':'U',
'v':'V',
'w':'W',
'x':'X',
'y':'Y',
'z':'Z',
'B':'b',
'C':'c',
'D':'d',
'E':'e',
'F':'f',
'G':'g',
'H':'h',
'I':'i',
'J':'j',
'K':'k',
'L':'l',
'M':'m',
'N':'n',
'O':'o',
'P':'p',
'Q':'q',
'R':'r',
'S':'s',
'T':'t',
'U':'u',
'V':'v',
'W':'w',
'X':'x',
'Y':'y',
'Z':'z',
}


def pressAForCapsLock(message):
    global alphabet_set
    global alphabet_dict
    caps_bool = 0
    final_string = ""
    for word in message:
        for char in word:
            if char in alphabet_set:
                if caps_bool:
                    final_string+=alphabet_dict[char]
                else:
                    final_string+=char
            else:
                if char == 'A' or char == 'a':
                    caps_bool = 1-caps_bool
                else:
                    final_string+=char
    
    return final_string

message = '"Baa, Baa!" said the sheep'

final_message = pressAForCapsLock(message)
print(final_message)