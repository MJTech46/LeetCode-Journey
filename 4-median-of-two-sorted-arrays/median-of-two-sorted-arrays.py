class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        nums3_len=len(nums3)

        if nums3_len%2==0:
            median=(nums3[int(nums3_len/2)]+nums3[int((nums3_len/2)-1)])/2
        else:
            median=nums3[int(nums3_len/2)]
        
        return median