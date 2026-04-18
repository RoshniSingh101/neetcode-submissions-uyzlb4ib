class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # edge case 1
            # if new interval goes before current interval
            # no overlapping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # edge case 2
            # if new interval goes after current interval
            # no overlapping
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # execute overlapping logic
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                            max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res
            

            