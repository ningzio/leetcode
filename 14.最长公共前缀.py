#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# algorithms
# Easy (43.74%)
# Likes:    3054
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#
#
# 示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
# 示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    return strs[0][:i]
        return strs[0]


# @lc code=end
if __name__ == "__main__":

    def test(input: List[str], want: str):
        got = Solution().longestCommonPrefix(input)
        assert got == want, f"input: {input}, want: {want}, got: {got}"

    test(["flower", "flow", "flight"], "fl")
    test(["dog", "racecar", "car"], "")
    test(["ab", "ac", "b"], "")
