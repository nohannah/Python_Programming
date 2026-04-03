# nums = list(map(int, input().split()))
# count = 0

# for x in nums:
#     if x > 5:
#         count += 1

# print(count)
# x = list(map(int, input().split()))
# for i in x:
#     if i % 2 == 0:
#      print("Even")
# else: 
#     print("odd")

# x=int(input())
# steps=x//5
# if x % 5 != 0: 
# 	steps = steps+1
# print(steps)
# 9
# a, b = map(int, input().split())
# year=0

# while a <=b:
#     a*=3
#     b*=2
#     year+=1
# print(year)

# n=int(input())
# count=0
# for i in range(0,n):
#     a, b, c = map(int, input().split())
#     if a+b+c >= 2:
#         count+= 1  
# print(count)

from typing import List

class solution:
    def twosum(self, num: List[int], target: int) -> List[int]:
        n=len(num)
        for i in range (n-1):
            for j in range (i+1,n):
                if num[i+j]== target:
                    return [i,j]         
        return ()
    