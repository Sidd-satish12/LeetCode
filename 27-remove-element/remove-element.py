class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        reverse_index = len(nums) - 1

        if reverse_index == -1:
            return 0

        if reverse_index == 0:
            if nums[index] == val:
                return 0
            else:
                return 1

        while index != reverse_index:
            if nums[index] == val:
                while nums[reverse_index] == val:
                    reverse_index -= 1
                    if index == reverse_index:
                        return index
                nums[index], nums[reverse_index] = nums[reverse_index], nums[index]
            index += 1
        if nums[-1] != val:
            index += 1
        return index



                    