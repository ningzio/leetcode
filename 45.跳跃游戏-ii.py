#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode.cn/problems/jump-game-ii/description/
#
# algorithms
# Medium (44.72%)
# Likes:    2384
# Dislikes: 0
# Total Accepted:    593.9K
# Total Submissions: 1.3M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j]
# 处:
#
#
# 0 <= j <= nums[i]
# i + j < n
#
#
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
#
#
#
# 示例 1:
#
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 示例 2:
#
#
# 输入: nums = [2,3,0,2,0,1]
# 输出: 2
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]
#
#
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        从起点和起点能跳过的最远距离中, 找到下一个能跳最远的作为落点
        记录跳的次数
        并记录跳的距离, 大于等于 nums.length 结束
        """
        count = 0
        i = 0
        while i < len(nums) - 1:
            count += 1
            if i + nums[i] >= len(nums) - 1:
                return count
            # 在 i + 1 ~ i + 1 + nums[i] 中寻找下一个落脚点
            # 能跳的最远的
            max_dis = 0
            for j in range(i + 1, i + 1 + nums[i]):
                dis = j + nums[j]
                # 提前结束
                if dis >= len(nums) - 1:
                    return count + 1
                if dis > max_dis:
                    max_dis = dis
                    i = j

        return count


# @lc code=end


if __name__ == "__main__":
    print(Solution().jump([2, 3, 0, 2, 1]))
