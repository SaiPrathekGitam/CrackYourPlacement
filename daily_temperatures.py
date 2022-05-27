class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = [0]
        answer = [0]*n
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp>temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day-prev_day
            stack.append(curr_day)
            
        return answer
        
