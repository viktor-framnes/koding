class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        x = set(nums)
        x = list(x)
        if len(x) < len(nums):
            return True
        else:
            return False
        
_ = Solution()
print(_.hasDuplicate([100,200,300,100,500,600,200]))
