#1. array > 3
#2. array starts in an increasing pattern
#3. array ends in decreasing pattern
#4. 
from typing import List

class Solution:
    def validMountain(self, mountain: List[int]) -> bool:
        i = 1
        if len(mountain) < 3:
            return False
        
        while (i < len(mountain) and mountain[i] > mountain[i-1] ):
            i += 1
        if (i == 1 or i == len(mountain)):
            return False

        while (i < len(mountain) and mountain[i-1] > mountain[i]):
            i += 1

        return i == len(mountain)

s=Solution()
answer = s.validMountain([1,2,2,4,3,1])

print(answer)