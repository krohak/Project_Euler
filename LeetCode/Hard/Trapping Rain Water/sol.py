class Solution:
    def trap(self, heights):
        
        n = len(heights)
        if not n:
            return 0
        
        left_heights = [heights[0]]
        for i in range(1,n):
            left_heights.append(max(left_heights[-1], heights[i]))
        
        
        right_heights = [0 for _ in range(n)]
        right_heights[n-1] = heights[n-1]
        for i in range(n-2, -1, -1):
            right_heights[i] = max(right_heights[i+1], heights[i])
        
        
        ans = 0
        
        for i in range(1, n-1):
            ans += min(left_heights[i], right_heights[i])-heights[i]
        
        return ans