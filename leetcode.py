class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [] #定义结果表
        hashtable={}#定义哈希表
        for i in range(len(nums)):
            hashtable[str(nums[i])] = i #为数组中每个数字进行哈希对应，键为值，值为索引
        for j in range(len(nums)):
            tmp = str(target-nums[j]) #求出对应数字的补数
            if tmp in hashtable.keys() and hashtable[tmp] != j: #如果补数在哈希表里且不等于当前值的
                result.append(j) #添加索引到结果表
                result.append(hashtable[tmp])#添加哈希表对应索引到结果表
                return sorted(result)

aa = Solution()
bb = [3,2,4]
c = 6
dd = aa.twoSum(bb,c)
print(dd)