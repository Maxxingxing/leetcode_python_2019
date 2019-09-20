class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__=="__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    #nums = [0,1,1]
    #nums=[1]
    s = Solution()
    print(s.removeDuplicates(nums))