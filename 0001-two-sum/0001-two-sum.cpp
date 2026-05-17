#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> my_dict;
        for (int i=0; i <= nums.size(); i++){
            int comp = target - nums[i];
            if (my_dict.find(comp) != my_dict.end()){
                  return {my_dict[comp], i};

            }
            my_dict[nums[i]] = i;

        }
        return {};          
    }    
};