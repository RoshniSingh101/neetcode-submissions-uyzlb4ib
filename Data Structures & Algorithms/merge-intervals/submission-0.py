class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O (n log n) time complexity including sorting

        # sort each pair interval by start value
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # get prev interval and the last value of prev interval
            lastEnd = output[-1][1]
            # equal counts as overlapping
            # merging logic
            # ex [1,6] and [3,5] merges into [1,6]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # otherwise, add interval if not overlapping
            else:
                output.append([start,end])
        return output