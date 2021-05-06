from typing import List

class Solution:
  def boatsave(self, people: List[int], limit: int) -> int:
      people.sort()  # [1,2,3,4,5]

      left = 0
      right = len(people) - 1

      boat_num = 0

      while ( left <= right ):  
          if left == right:
             boat_num += 1
             break
          if ( people[left]+people[right] <= limit ):
             left += 1

          right -= 1

          boat_num += 1
      return boat_num

s=Solution()
answer = s.boatsave([1,1,5],10)

print(answer)
             
