/**
 * @param {number[]} nums
 * @return {number}
 */
 const singleNumber = (nums) => {
    let res = 0;
    
    nums.forEach(num => {res ^= num;});
        
    return res;
};