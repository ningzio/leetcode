#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
# https://leetcode.cn/problems/gas-station/description/
#
# algorithms
# Medium (49.31%)
# Likes:    1478
# Dislikes: 0
# Total Accepted:    306.2K
# Total Submissions: 621.4K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一
# 的。
#
#
#
# 示例 1:
#
#
# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#
# 示例 2:
#
#
# 输入: gas = [2,3,4], cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
#
#
#
# 提示:
#
#
# gas.length == n
# cost.length == n
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
#
#
#

# @lc code=start
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t = 0
        s = -1
        t1 = 0  # 从 s 开始计算剩余的汽油

        for i in range(len(gas)):
            t = t + gas[i] - cost[i]  # 总消耗

            # 从当前站到下一站需要的消耗
            currentCost = gas[i] - cost[i]

            if t1 + currentCost < 0:
                # 之前积累的汽油无法走到下一站
                s = -1
                t1 = 0
            else:
                t1 += currentCost
                s = i if s == -1 else s
        return s if t >= 0 else -1


# @lc code=end

if __name__ == "__main__":

    def test(gas: List[int], cost: List[int], result: int):
        res = Solution().canCompleteCircuit(gas=gas, cost=cost)
        assert (
            res == result
        ), f"gas: {gas}, cost: {cost}, expected: {result}, got: {res}"

    test([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3)
    test([4, 1, 3], [1, 5, 2], 2)


# gas = [1,2,3,4,5], cost = [3,4,5,1,2]
#       [-2, -2, -2, 3, 3]
# gas = [2,3,4], cost = [3,4,3]
#       [-1, -1, 1]

# [-1, 2, -1, 1, -2, 1]

# [4, 1, 3]  [1, 5, 2]
# i = index
# total = 0  总剩余, 最后如果小于 0, 此题无解
# start = -1  开始的位置

# i = 0
#   total = 4 - 1 = 3
#   start = 0   # total 大于 0, 乐观一点
# i = 1
#   total = 3 + 1 - 5 = -1
#   start = -1  # total 小于 0, 说明前面累积的所有汽油都不够走完这个路程
# i = 2
#   total = -1 + 3 - 2 = 0
#   start = 2
