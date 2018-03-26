#1两数之和给定一个整数数列，找出其中和为特定值的那两个数。

#你可以假设每个输入都只会有一种答案，同样的元素不能被重用。
#
#
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         result = [] #定义结果表
#         hashtable={}#定义哈希表
#         for i in range(len(nums)):
#             hashtable[str(nums[i])] = i #为数组中每个数字进行哈希对应，键为值，值为索引
#         for j in range(len(nums)):
#             tmp = str(target-nums[j]) #求出对应数字的补数
#             if tmp in hashtable.keys() and hashtable[tmp] != j: #如果补数在哈希表里且不等于当前值的
#                 result.append(j) #添加索引到结果表
#                 result.append(hashtable[tmp])#添加哈希表对应索引到结果表
#                 return sorted(result)
#
#
# #2、给定一个范围为 32 位 int 的整数，将其颠倒。
# #假设我们的环境只能处理 32 位 int 范围内的整数。根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。
#
# class Solution1(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         sign = -1 if x < 0 else 1  #先判断数字的正负数先把正负符号搞定
#         result = int(str(abs(x))[::-1])#数字转化为绝对值字符串格式然后反转
#         if result > 2 ** 31 -1: #如果数字大于32位整数范围，返回0
#             return 0
#         else:
#             return result *sign #否则返回结果加上正负号

#3、判断一个整数是否是回文数。不能使用转化为字符串辅助空间。
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False #如果一个数小于0 就不是回文数
    b = x
    ans = 0
    while x > 0:
        ans = ans*10 + x%10
        if x > 2**31-1:
            return False
        x //= 10
    if ans == b:
        return True
    return False
