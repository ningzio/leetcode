#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List

# [1, 2, 3, 4, 5]


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r, cnt = 0, len(nums) - 1, len(nums)
        while l <= r:
            if nums[l] == val:
                # 右指针左移, 找到第一个不等于 val 的值进行替换
                while r > l and nums[r] == val:
                    cnt -= 1
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
                cnt -= 1
                r -= 1
            l += 1
        return cnt


# @lc code=end


if __name__ == "__main__":
    print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
    print(Solution().removeElement(nums=[2], val=2))
    print(Solution().removeElement(nums=[2], val=3))
