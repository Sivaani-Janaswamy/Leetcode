class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        hashmap = {}
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
            else:
                while(stack and nums2[i]>stack[-1]):
                    hashmap[stack.pop()] = nums2[i]
                stack.append(nums2[i])
        res = []
        for i in nums1:
            if i in hashmap:
                res.append(hashmap[i])
            else:
                res.append(-1)
        return res

        