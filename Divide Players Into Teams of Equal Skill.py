class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        val = skill[0] + skill[-1]
        s = skill[0] * skill[-1]
        for i in range(1,(n//2)):
            j = (n-1)-i
            if skill[i]+skill[j] != val:
                return -1
            s += skill[i]*skill[j]
        return s

            

