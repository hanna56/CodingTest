class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        for i in range(min([len(i) for i in strs])):
            val = 0
            for j in range(len(strs)):
                if j == len(strs)-1:
                    break
                if strs[j][i] != strs[j+1][i]:
                    val = 1
                    break
            if val == 0:
                answer+= strs[0][i]
            else:
                break
        return answer
