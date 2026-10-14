from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}  # 값 -> 인덱스
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []