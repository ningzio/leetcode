#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cursor = m + n - 1
        m -= 1
        n -= 1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[cursor] = nums1[m]
                m -= 1
            else:
                nums1[cursor] = nums2[n]
                n -= 1
            cursor -= 1

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        双指针控制 nums1 和 nums2 的索引从后往前移动
        cursor 控制 nums1 指针从后往前移动, 直到等于 0

        通过比较 nums1 和 nums2 的最后面的值的大小, 放入 cursor 的位置
        """
        cursor = m + n
        while cursor > 0:
            cursor -= 1
            if m == 0:
                nums1[cursor] = nums2[n - 1]
                n -= 1
                continue
            elif n == 0:
                break

            i, j = nums1[m - 1], nums2[n - 1]
            if i > j:
                nums1[cursor] = i
                m -= 1
            else:
                nums1[cursor] = j
                n -= 1


if __name__ == "__main__":
    #    0  1  2  3  4  5
    x = [7, 8, 9, 0, 0, 0]
    y = [10, 12, 13]
    Solution().merge(x, 3, y, 3)
    print(x)

# @lc code=end
