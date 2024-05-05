class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [time, 1] -> start 
        # [time, -1] -> end
        # sort
        tmp, count, res = [], 0, 0
        for interval in intervals:
            tmp.append([interval[0], 1])
            tmp.append([interval[1], -1])
        
        tmp.sort()
        for _, val in tmp:
            count += val
            res = max(res, count)
        
        return res
