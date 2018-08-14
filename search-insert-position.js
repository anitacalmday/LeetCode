/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
     let out = nums.indexOf(target);
     if (out == -1){
        let i = 0
        for (; target > nums[i] ; i++){};
        out = i;
    }
    return out ;
};
