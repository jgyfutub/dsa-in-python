class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=0
        overall_max=-inf
        for num in nums:
            curr_max=max(curr_max+num,num)
            overall_max=max(overall_max,curr_max)
        return overall_max
