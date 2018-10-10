class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        newstr = A + " " + B
        stringArr = []
        stringArr = newstr.split()
        Dict = {}
        res = []
        for word in stringArr: 
            if word in Dict: 
                Dict[word] +=1
            else: 
                Dict[word] = 1
        for words in Dict: 
            if Dict[words] == 1: 
                res.append(words)
        return res
