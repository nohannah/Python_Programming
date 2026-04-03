from typing import List
class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        maxsum=-float["inf"]
        n=len(num)
        for i in range(n):
            for j in range(i+1,n+1):
                sum=sum(num[i:j])
                maxsum=max(maxsum,sum)
        return maxsum
 