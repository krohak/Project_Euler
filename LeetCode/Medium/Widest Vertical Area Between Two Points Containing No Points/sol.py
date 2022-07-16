class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        sortedXCords = sorted(set(map(lambda x: x[0], points)))
        spaces = [ sortedXCords[i] - sortedXCords[i-1] for i in range(1, len(sortedXCords)) ]
        return max(spaces) if spaces else 0