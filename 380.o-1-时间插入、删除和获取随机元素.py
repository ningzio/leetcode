#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
# https://leetcode.cn/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (52.39%)
# Likes:    757
# Dislikes: 0
# Total Accepted:    132.1K
# Total Submissions: 252.1K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
#  '[[],[1],[2],[2],[],[1],[2],[]]'
#
# 实现RandomizedSet 类：
#
#
#
#
# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
#
#
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
#
#
#
# 示例：
#
#
# 输入
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出
# [null, true, false, true, 2, true, false, 2]
#
# 解释
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
#
#
#
#
# 提示：
#
#
# -2^31 <= val <= 2^31 - 1
# 最多调用 insert、remove 和 getRandom 函数 2 * 10^5 次
# 在调用 getRandom 方法时，数据结构中 至少存在一个 元素。
#
#
#
#
#


# @lc code=start
from collections import defaultdict
import random


class RandomizedSet:
    def __init__(self):
        self.m = dict()
        self.l = list()
        self.count = 0
        self.rand = self._get_random()

    def _get_random(self) -> int:
        return random.randint(0, 1 << 64 - 1)

    def insert(self, val: int) -> bool:
        # 已存在
        if self.m.get(val, -1) >= 0:
            return False
        self.l.append(val)
        self.m[val] = self.count
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        index = self.m.get(val, -1)
        # 不存在
        if index < 0:
            return False

        # 如果是最后有一个元素, 直接移除
        if index == self.count - 1:
            self.l.pop()
        else:
            # 最后一个元素移动到 index 处并移除最后一个元素
            last = self.l.pop()
            self.l[index] = last
            self.m[last] = index
        del self.m[val]
        self.count -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)
        # if self.count == 0:
        #     return None
        # res = self.l[(self.rand % self.count) - 1]
        # self.rand >>= 1
        # if self.rand == 0:
        #     self.rand = self._get_random()
        # return res


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end


if __name__ == "__main__":
    obj = RandomizedSet()

    obj.insert(1)
    obj.insert(10)
    obj.insert(20)
    obj.insert(30)

    d = defaultdict(int)

    for i in range(1000):
        x = obj.getRandom()
        d[x] += 1

    for k, v in d.items():
        print(f"{k}: {v / 1000 * 100}%")
