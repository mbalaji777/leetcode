def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexer = 1
    for element in nums:
        if (target-element) in nums[indexer:]:
            return [nums.index(element), nums.index(target-element)]
        indexer+=1
    return -1

if __name__ == "__main__":
    nums = [3,3]
    target = 6
    x = twoSum(nums, target)
    print(x)
