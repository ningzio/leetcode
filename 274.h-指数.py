#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
# https://leetcode.cn/problems/h-index/description/
#
# algorithms
# Medium (46.37%)
# Likes:    434
# Dislikes: 0
# Total Accepted:    137.9K
# Total Submissions: 297.5K
# Testcase Example:  '[3,0,6,1,5]'
#
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
#
# 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h
# 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
#
#
#
# 示例 1：
#
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
#
# 示例 2：
#
#
# 输入：citations = [1,3,1]
# 输出：1
#
#
#
#
# 提示：
#
#
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
#
#
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        [3, 0, 6, 1, 5]
        [1, 0, 1, 0, 2]

        """
        n = len(citations)
        l = [0] * (n + 1)

        for c in citations:
            if c > n:
                l[n] += 1
            else:
                l[c] += 1

        h = 0
        for i in range(n, 0, -1):
            h += l[i]
            if h >= i:
                return i
        return 0

    def hIndex1(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        h = length
        while h > 0:
            # 至少需要 h 篇论文的引用次数大于 h
            # 排序后的论文列表中, 如果 citations[length - h -1] 位置处的引用次数小于 h
            # 则不满足条件
            if citations[length - h] >= h:
                return h
            h -= 1
        return 0


# @lc code=end


def test(input, expect):
    assert (
        Solution().hIndex(input) == expect
    ), f"input: {input}, result: {Solution().hIndex(input)}, expect: {expect}"


if __name__ == "__main__":
    test([0, 1], 1)
    test([100], 1)
    test([0], 0)
    test([1, 3, 1], 1)
    test([3, 0, 6, 1, 5], 3)

    print("pass")
