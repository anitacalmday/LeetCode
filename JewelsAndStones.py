class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Dict = {}
        jewelCounter = 0
        for char in S: 
            if char in Dict: 
                Dict[char] += 1
            else: 
                Dict[char] = 1
        for char in J: 
            if char in Dict: 
                
                jewelCounter += Dict.get(char)
           
        return jewelCounter
