from collections import defaultdict

userIdi = 0
businessIdi = 1

class Solution:
    
    def findMostSimilarBusiness(self, businessOfInterestId, positiveReviews):
        
        businessReviewsDict = defaultdict(set)
        for review in positiveReviews:
            businessReviewsDict[review[businessIdi]].add(review[userIdi])

        boiReviews = businessReviewsDict[businessOfInterestId]

        maxSimilarity, maxSimilarBusiness = 0, float("inf")
        for business, reviews in businessReviewsDict.items():
            if not business == businessOfInterestId:
                similarity = len(boiReviews.intersection(reviews)) / len(boiReviews.union(reviews))
                if similarity>maxSimilarity:
                    maxSimilarity = similarity
                    maxSimilarBusiness = business

        return maxSimilarity, maxSimilarBusiness


if __name__ == '__main__':
	positiveReviews = [(1,10),(2,10),(1,11),(2,11),(1,12),(2,12),(3,12)]
	print(Solution().findMostSimilarBusiness(10,positiveReviews))