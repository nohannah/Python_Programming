from typing import List

class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(num)):
            complement = target - num[i]

            if complement in d:
                return [d[complement], i]

            d[num[i]] = i
# get input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

s = Solution()
result = s.twoSum(nums, target)

print("Indices:", result)