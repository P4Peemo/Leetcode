#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        n = len(s)
        one_word_len, word_num = len(words[0]), len(words)
        words = Counter(words)
        left = right = 0
        ans = []
        for i in range(one_word_len):
            left = i
            right = i
            curr_count = 0
            curr_counter = Counter()
            while right + one_word_len <= n:
                part = s[right:right + one_word_len]
                right += one_word_len

                if part not in words:
                    left = right
                    curr_counter.clear()
                    curr_count = 0
                else:
                    curr_counter[part] += 1
                    curr_count += 1
                    while curr_counter[part] > words[part]:
                        left_part = s[left:left+one_word_len]
                        left += one_word_len
                        curr_counter[left_part] -= 1
                        curr_count -= 1
                    if curr_count == word_num:
                        ans.append(left)
        return ans

# @lc code=end

