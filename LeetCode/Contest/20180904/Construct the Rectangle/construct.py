from numpy import sqrt



class Solution(object):
    def constructRectangle(self, area):
        
        # area = int(input())

        res_list = []
        for x in reversed(range(1,int(sqrt(area)+1))):
            print(x)

            if area % x == 0:
                res_list.append((x, area//x))


        print(res_list)

        res_tup = ()
        diff = area
        for tup in res_list:
            tup_diff = abs(tup[0] - tup[1])
            if tup_diff < diff:
                res_tup = tup
                diff = tup_diff

        res_list = [ max(res_tup) , min(res_tup) ]

        # print(res_list)
        return res_list
