#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
         [1, 1, 3, 5]
         p1
             p2

         [1, 1, 3, 5]
         p1
                p2

         [1, 3, 3, 5]
             p1
                   p2

        [1, 3, 5, 5]
               p1
                  p2
        """
        p1 = 0
        for p2 in range(1, len(nums)):
            if nums[p1] == nums[p2]:
                continue
            nums[p1 + 1] = nums[p2]
            p1 += 1
        return p1 + 1


# @lc code=end


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2]))
