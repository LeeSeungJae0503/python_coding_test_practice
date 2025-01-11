class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = []
            dic[num].append(index)
        
        for v in dic:
            n = target - v
            if n in dic:
                if v != n:
                    return [dic[v][0], dic[n][0]]
                elif len(dic[n]) > 1:
                    return [dic[n][0], dic[n][1]] 
        return False
    

"""
class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in dic:
                return [dic[complement], i]
            dic[n] = i
        return False
"""