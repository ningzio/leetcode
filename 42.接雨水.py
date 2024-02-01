#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (63.18%)
# Likes:    4967
# Dislikes: 0
# Total Accepted:    843.9K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left, right = 0, 2
        stack = []
        while right < len(height):
            if height[left] < height[left + 1]:
                left += 1
                right += 1
                continue
            if height[right] <= height[right - 1]:
                right += 1
                continue
            x = min(height[left], height[right])
            rain = 0
            for i in height[left + 1 : right]:
                if height[i] < x:
                    rain += x - height[i]
            cor = [left, right, rain]
            for i in range(len(stack)):
                prev = stack[i]
                if height[right] > height[left] and prev[0] > height[left]:
                    rain = 0
                    x = min(height[right], height[prev[0]])
                    for j in range(height[prev[0]], height[right]):
                        if height[j] < 0:
                            rain += x - height[j]
                    cor[0] = prev[0]
                    cor[2] = rain
                    stack = stack[:i]
                    break
            stack.append(cor)

            left = right
            right = right + 2

        return sum([i[2] for i in stack])


# @lc code=end


if __name__ == "__main__":

    def test(input: List[int], expect: int):
        res = Solution().trap(input)
        assert res == expect, f"input: {input}, expect: {expect}, got: {res}"

    test([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
