#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        
        if dividend == 0:
            return 0
        
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        def quickAdd(y: int, z: int, x: int) -> bool:
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    if add < x - add:
                        return False
                    add += add
                z >>= 1
            return True
        
        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1
        return -ans if rev else ans

# @lc code=end

