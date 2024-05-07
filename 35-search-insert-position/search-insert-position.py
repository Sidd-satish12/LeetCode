class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = len(nums)//2

        if len(nums) <= 2:
            if nums[index] == target:
                return index
            if nums[0] == target:
                return 0
            if target > nums[index] and len(nums) == 2:
                return 2
            elif target > nums[index]:
                return 1
            if target < nums[0]:
                return 0
            else:
                return 1
        if nums[index] == target:
            return index
        elif nums[index] > target:
            print(index)
            index = self.searchInsert(nums[0:index],target)
        elif nums[index] < target:
            index += self.searchInsert(nums[index:],target)
        return index
        