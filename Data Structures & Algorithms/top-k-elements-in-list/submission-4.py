class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for x in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # if len(nums) == k:
        #     return nums
        # hashmap = {}
        # list_set = set(nums)
        # res = []
        # for x in list_set:
        #     hashmap.setdefault(nums.count(x), []).append(x)
        # print(hashmap)
        # while k > 0:
        #     for x in hashmap[(max(hashmap))]:
        #         print(x)
        #         res.append(x)
        #         k -= 1
        #     hashmap.pop(max(hashmap))
        # return res