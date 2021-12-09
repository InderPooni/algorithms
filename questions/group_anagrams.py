from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list)

    for s in strs:
        sorted_s = "".join(sorted(s))

        res[sorted_s].append(s)
    
    return res.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))