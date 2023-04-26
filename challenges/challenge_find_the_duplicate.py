def find_duplicate(nums):
    nums.sort()

    for index in range(1, len(nums)):
        if type(nums[index]) == str or int(nums[index]) < 0:
            return False

        if nums[index] == nums[index - 1]:
            return nums[index]

    return False
