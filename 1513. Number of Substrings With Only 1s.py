Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.
Example 1:
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        st = s.split('0')
        for i in st:
            cnt += i.count('1')*(i.count('1') + 1)//2
        return cnt%(10**9 + 7)
#or
class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        consecutive = 0
        for i in range(len(s)):
            if s[i] == '1':
                consecutive += 1
                cnt += consecutive
            else:
                consecutive = 0
        return cnt % (10**9 + 7)
