from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]

        return hare
