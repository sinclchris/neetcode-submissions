class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for i in range(len(strs)):
            key = str(sorted(strs[i]))
            val = strs[i]
            if key in mydict:
                mydict[key].append(val)
            else:
                mydict[key] = [val]
        return list(mydict.values())
        



