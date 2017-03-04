"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        ret_lst = []
        if nums_len < 2:
            return ret_lst
        if not isinstance(target, int):
            return ret_lst

        idx_tbl = dict()
        for idx, num in enumerate(nums):
            if num in idx_tbl:
                idx_tbl[num] = (idx_tbl[num], idx,)
            else:
                idx_tbl[num] = idx

        nums = sorted(nums)
        for idx, num in enumerate(nums):
            the_other = target - num
            found = self.binary_search(nums[idx+1:nums_len], the_other)
            if found != -1:
                if num == the_other and isinstance(idx_tbl[num], tuple):
                    ret_lst.append(idx_tbl[num][0])
                    ret_lst.append(idx_tbl[num][1])
                else:
                    ret_lst.append(idx_tbl[num])
                    ret_lst.append(idx_tbl[found])
                break

        return ret_lst

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if target == nums[mid]:
                return nums[mid]
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

