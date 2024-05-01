class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index in range(0,n):
            nums1[m + index] = nums2[index]
        nums1.sort()
        