#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, m
        median_l, median_r = 0, 0
        inf = 2**40

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            pre_index_i = -inf if i == 0 else nums1[i - 1]
            index_i = inf if i == m else nums1[i]
            pre_index_j = -inf if j == 0 else nums2[j - 1]
            index_j = inf if j == n else nums2[j]

            if pre_index_i <= index_j:
                median_l, median_r = max(pre_index_i, pre_index_j), min(index_i, index_j)
                l = i + 1
            else:
                r = i - 1
            
        return (median_l + median_r) / 2 if (m + n) % 2 == 0 else median_l

# @lc code=end

