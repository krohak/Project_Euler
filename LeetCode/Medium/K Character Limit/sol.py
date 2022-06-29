def cropSentence(sentence, k):
    if k < 1:
        return ""
    count = 0
    output = []
    res = [i for j in sentence.split() for i in (j, ' ')][:-1]
    for word in res:
        if count >= k:
            return ' '.join([ w for w in output if w !=" " ])
        count += len(word)
        if count <= k:
            output.append(word)
    return ' '.join([ w for w in output if w !=" " ])


# test = "Codility We test coders"
# K = 14
# print(len(cropSentence(test, K)))

# test = "The quick brown fox jumps over the lazy dog"
# K = 39
# print(cropSentence(test, K))

test="To crop or not to crop"
K = 21
print(len(cropSentence(test, K)))