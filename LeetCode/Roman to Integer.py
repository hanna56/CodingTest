class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        answer = 0
        pre = ""
        for i in s:
            if pre != "" and sym[i] > sym[pre]:
                answer += sym[i] - sym[pre]
                pre = ""
            elif pre !="" and sym[i] <= sym[pre]:
                answer += sym[pre]
                pre = i
            elif pre == "":
                pre = i
        if pre != "":
            answer += sym[pre]
        return answer
            
            
