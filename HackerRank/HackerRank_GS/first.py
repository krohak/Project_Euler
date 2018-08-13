


scores = [1, 2, 2, 3]


def findMaxGoalsProbability(teamGoals):
    
    n = len(teamGoals)
    if n<=1:
        return "0.00"

    match_scores = []

    i=0
    while i<n:
        j = i+1
        while j<n:
            match_scores.append(teamGoals[i]+teamGoals[j])
            j+=1
        i+=1
        
    print(match_scores)

    max_score = max(match_scores)
    if max_score == 0:
        return "0.00"

    occurances = sum([1 for i in match_scores if i==max_score])

    print(occurances)
    prob = occurances/len(match_scores)

    print("{0:.2f}".format(prob))

    return "{0:.2f}".format(prob)


prob = findMaxGoalsProbability(scores)