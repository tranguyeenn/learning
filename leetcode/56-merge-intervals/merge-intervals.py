class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged = []

        cur_start, cur_end = intervals[0]

        for s, e in intervals[1:]:
            if s <= cur_end:
                cur_end = max(cur_end, e)
            else:
                merged.append([cur_start, cur_end])
                cur_start, cur_end = s,e 

        merged.append([cur_start, cur_end]) 
        return merged       