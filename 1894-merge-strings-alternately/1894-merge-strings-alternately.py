class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word3 = []
        len1,len2 = len(word1),len(word2)
        max1 = max(len1,len2)

        for i in range(max1):
            if i < len1:
                word3.append(word1[i])
            if i < len2:
                word3.append(word2[i])
        return ''.join(word3)

        