class Solution {
    public int[] productExceptSelf(int[] nums) {
        int mult=1;
        int zero_counter = 0;
        for(int num:nums){
            if(num!=0){
                mult*=num;
            }
            else{
                zero_counter++;
            }
        }
        int [] output = new int [nums.length];
        if(zero_counter>1) return output;
        for(int i=0;i<nums.length;i++){
            if(zero_counter==1 && nums[i]!=0) output[i]=0;
            else{
                int divider = nums[i]==0?1:nums[i];
                output[i]=mult/divider;
            }
        }
        return output;
    }
}  
