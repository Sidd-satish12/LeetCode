class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        j = 0
        interval = 1
        for i in range(0, len(nums)):
            try:
                if nums[j] == nums[i + 1] - interval:
                    interval += 1
                    continue
                else:
                    if interval == 1:
                        output.append(str(nums[j]))
                    else:
                        output.append(str(nums[j]) + "->" + str(nums[i]))
                    j = i + 1
                    interval = 1
            except IndexError:
                if interval == 1:
                    output.append(str(nums[j]))
                else:
                    output.append(str(nums[j]) + "->" + str(nums[i]))
        return output