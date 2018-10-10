from heapq import heappush, heappop
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqDict = {}
     
        for i in nums: 
            if i in freqDict: 
                freqDict[i] += 1; 
            else: 
                freqDict[i] =1; 
        
        heap = []
        for key in freqDict:
            heappush(heap, (freqDict[key], key))
    
        while len(heap)>k:
            heappop(heap)
            
        results = []
        while heap:
            results.append(heappop(heap)[1])
            results.reverse()
        return results
            
           
