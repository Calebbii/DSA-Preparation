function removeDuplicates(nums) {
    let count = 1;
    let duplicateCount = 1;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            duplicateCount++;
        } else {
            duplicateCount = 1;
        }

        if (duplicateCount <= 2) {
            nums[count] = nums[i];
            count++;
        }
    }

    return count;
}
let nums1 = [1, 1, 1, 2, 2, 3];
console.log(removeDuplicates(nums1)); // Output: 5, nums1 = [1, 1, 2, 2, 3]

let nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3];
console.log(removeDuplicates(nums2)); // Output: 7, nums2 = [0, 0, 1, 1, 2, 3, 3]