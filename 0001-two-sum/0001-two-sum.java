import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> my_dict = new HashMap<>();
        for (int i = 0; i <= nums.length; i++){
            int comp = target - nums[i];
            if (my_dict.containsKey(comp)){
                return new int[]{my_dict.get(comp), i};
            }
            my_dict.put(nums[i], i);
        }
        return new int[0];
        
    }
}