from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g > 1:
                    num = stack.pop() * num // g
                else:
                    break
            stack.append(num)
        return stack