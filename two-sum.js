/* Given an array of integers, return indices of the two numbers such that they add up to a specific target. */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var sumArr = []; 
    for (var i = 0; i < nums.length; i++){
        for (var j = 0; j < i ; j++)
            {
                if (nums[i] + nums[j] == target){
                        sumArr.push(i); 
                        sumArr.push(j); 
                }
            }
    }
    return sumArr; 
};
