class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hash = new HashMap<>();
        int[] arr = {0,0};
        for(int i = 0;i<nums.length;i++){
            if(hash.containsKey(target-nums[i])){
              arr[0] = hash.get(target-nums[i]);
              arr[1] = i;
              break;
            }
            hash.put(nums[i],i);
        }
        return arr;
    }
}