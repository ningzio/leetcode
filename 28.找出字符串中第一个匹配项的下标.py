#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (43.24%)
# Likes:    2137
# Dislikes: 0
# Total Accepted:    991.3K
# Total Submissions: 2.3M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
#
#
#
# 示例 1：
#
#
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
#
#
# 示例 2：
#
#
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#
#
#
#
# 提示：
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
#
#
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            # 从 i 开始的字符串长度不足
            if len(haystack) - i < len(needle):
                return -1

            x, y = 0, len(needle) - 1
            while x <= y:
                if needle[x] == haystack[i + x] and needle[y] == haystack[i + y]:
                    if x >= y or y - x == 1:
                        return i
                    x += 1
                    y -= 1
                # 不符合条件
                else:
                    break
        return -1


# @lc code=end
if __name__ == "__main__":

    def test(haystack: str, needle: str, want: int):
        got = Solution().strStr(haystack, needle)
        assert want == got, f"input: {haystack} - {needle}, want: {want}, got: {got}"

    test("leetcode", "leeto", -1)
    test("sadbutsad", "sad", 0)
    test("hello", "ll", 2)
    test("abc", "c", 2)
    test("mississippi", "issi", 1)
    test("babba", "bbb", -1)
