class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        # print(count)
        # print(freq)
        print(count.get(4,0))
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                

print(Solution().topKFrequent([1,2,2,3,3,3],2))