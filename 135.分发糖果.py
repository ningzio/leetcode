#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode.cn/problems/candy/description/
#
# algorithms
# Hard (49.52%)
# Likes:    1418
# Dislikes: 0
# Total Accepted:    269.1K
# Total Submissions: 543.4K
# Testcase Example:  '[1,0,2]'
#
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
#
#
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
#
#
# 示例 1：
#
#
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
#
#
# 示例 2：
#
#
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
#
#
#
# 提示：
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#

# @lc code=start
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 初始时一定给第一个孩子一颗糖果
        candies = 1
        given = 1
        down = 0  # 下降趋势
        for i in range(1, len(ratings)):
            cur, prev = ratings[i], ratings[i - 1]

            # 评分比上一个孩子高, 要多给一个糖果
            if cur > prev:
                given += 1
                candies += given
            # 评分比上一个孩子低, 要少给一个糖果
            elif cur < prev:
                given -= 1
                # 每个孩子最少得到一颗糖果, 此时需要回溯
                if given == 0:
                    pass
            # 评分一样高
            else:
                if given == 1:
                    given += 1
                else:
                    given = 1


# @lc code=end


"""
5 4 3 3 3
1           1
2 1         3
3 2 1       6
3 2 1 2     8
3 2 1 2 1   9

"""
