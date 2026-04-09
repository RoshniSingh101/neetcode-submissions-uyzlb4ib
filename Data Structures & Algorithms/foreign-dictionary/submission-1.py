class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # for each word in words and character in each word
        # we want to map each character to a set
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            # checks if first word is longer than second
            # and if both share the same prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                # if characters are different
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # add to adjacency list
                    break

        visit = {} # False means character visited, True means visited and in current path
        res = []

        # post order dfs
        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True # detected loop

            visit[c] = False
            res.append(c)

        # go thru each character in adjacency list
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)