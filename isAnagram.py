class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        Dict = {}
        if len(s) != len(t): 
            return False
       
        for item in s: 
            if item in Dict:
                Dict[item] += 1
            else: 
                Dict[item] = 1
                
        for item in t: 
            if item in Dict:
                Dict[item] -= 1
                if Dict[item] == 0: 
                    del Dict[item]
            else:
                Dict[item] = 1
              
        if len(Dict) > 0: 
            return False
        return True 
