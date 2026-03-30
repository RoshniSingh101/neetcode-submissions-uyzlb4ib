class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        hashmap = {}
        list_set = set(nums)
        res = []
        for x in list_set:
            hashmap.setdefault(nums.count(x), []).append(x)
        print(hashmap)
        while k > 0:
            for x in hashmap[(max(hashmap))]:
                print(x)
                res.append(x)
                k -= 1
            hashmap.pop(max(hashmap))
        return res