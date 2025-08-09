class Solution {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        int trueSum = (len*(len+1))/2;
        int realSum = 0;
        for(int i:nums){
            realSum+=i;
        }
        return trueSum-realSum;
    }
}