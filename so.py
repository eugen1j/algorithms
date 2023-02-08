class Solution:
    def canBeIncreasing(self, nums) -> bool:
        dec_idx = None
        for (idx_l, val_l), (idx_r, val_r) in zip(enumerate(nums), enumerate(nums[1:], 1)):
            if val_l >= val_r:
                if dec_idx is not None:
                    return False
                dec_idx = (idx_l, idx_r)

        if dec_idx is None:
            return True

        if idx_l == 0 or idx_r == len(nums) - 1:
            return True

        return nums[idx_l - 1] < nums[idx_r] or nums[idx_l] < nums[idx_r + 1]


Solution().canBeIncreasing([2,3,1,2])
