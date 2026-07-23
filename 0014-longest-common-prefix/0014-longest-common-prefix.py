class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in strs[1:]:

            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix        