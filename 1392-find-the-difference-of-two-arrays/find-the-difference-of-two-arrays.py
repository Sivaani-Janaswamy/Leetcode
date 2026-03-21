class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        answers = []
        answers.append(list(s1-s2))
        answers.append(list(s2-s1))
        return answers