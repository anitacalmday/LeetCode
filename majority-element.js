/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var mymap = new Map(); 
    
    for (var i = 0; i < nums.length; i++) {
        if (mymap.get(nums[i]) == undefined) {
             mymap.set(nums[i], 1);
        }
        else {
            mymap.set(nums[i], mymap.get(nums[i])+1);
        }
    }
    
    var maxFreq = 0;
    var maxElem = 0;
    
    function findMaxFreq(value, key, map) {
        if(value > maxFreq){
            maxFreq = value;
            maxElem = key;
        }
    }
    mymap.forEach(findMaxFreq) 
    
    return maxElem
};
