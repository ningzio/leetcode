#
# @lc app=9leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode.cn/problems/zigzag-conversion/description/
#
# algorithms
# Medium (52.52%)
# Likes:    2265
# Dislikes: 0
# Total Accepted:    640.5K
# Total Submissions: 1.2M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
#
# string convert(string s, int numRows);
#
#
#
# 示例 1：
#
#
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
#
# 示例 2：
#
#
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# 示例 3：
#
#
# 输入：s = "A", numRows = 1
# 输出："A"
#
#
#
#
# 提示：
#
#
# 1
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1
#
#
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        ans = s[0]
        l = []
        start = 0
        while True:
            nextIndex = start + (numRows - 1) * 2
            l.append([start, nextIndex])
            if nextIndex >= len(s):
                break
            ans += s[nextIndex]
            start = nextIndex

        i = 0
        while i < len(l):
            a, b = l[i][0] + 1, l[i][1] - 1
            if a >= len(s):
                i += 1
                continue
            if a == b:
                ans += s[a]
            else:
                ans += s[a]
                if b < len(s):
                    ans += s[b]
                l.append([a, b])
            i += 1
        return ans


# @lc code=end


if __name__ == "__main__":

    def test(input: str, rows: int, want: str):
        got = Solution().convert(input, rows)
        assert want == got, f"input: {input}, want: {want}, got: {got}"

    # test("ABCDEFGHIJKLMN", 2, "ACEGIKMBDFHJLN")
    # test("ABCDEFGHIJKLMN", 3, "AEIMBDFHJLNCGK")
    # test("ABCDEFGHIJKLMN", 4, "AGMBFHLNCEIKDJ")
    test("AB", 1, "AB")


"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13
A B C D E F G H I J K  L  M  N


N = 2 X = 1

---

0   2   4   6   8   10  12
A   C   E   G   I   K   M
| / | / | / | / | / | / |
1   3   5   7   9   11  13
B   D   F   H   J   L   N

---

0       4       8        12
A       E       I        M
|     / |     / |      / |
1   3   5   7   9   11   13
B   D   F   H   J   L    N
| /     | /     |  /
2       6       10
C       G       K

---

0            6            12
A            G            M
|          / |          / |
1        5   7        11  13
B        F   H        L   N
|      /     |      /
2    4       8   10
C   E        I   K
| /          | /
3            9
D            J

---



0               8
A               I
|             / |
1           7   9
B           H   J
|         /     |
2       6       10
C       G       K
|     /         |
3   5           11   13
D   F           L    N
| /             |  /
4               12
E               M


"""
