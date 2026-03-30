class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            temp = ''.join(sorted(x))
            hashmap.setdefault(temp, []).append(x)
        return list(hashmap.values())