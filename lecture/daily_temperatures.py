# https://leetcode.com/problems/daily-temperatures/description/
class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []

        for current_day, current_temp in enumerate(temperatures):
            while stack and stack[-1][1] < current_temp:
                prev_day, _ = stack.pop()
                ans[prev_day] = current_day - prev_day
            stack.append((current_day, current_temp))
        return ans