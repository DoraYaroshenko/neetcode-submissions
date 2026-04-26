class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<Integer> numsList = Arrays.stream(nums).boxed().collect(Collectors.toList());
        HashSet<List<Integer>> tripletsSet = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                HashSet<Integer> numsSet = new HashSet<>(numsList.subList(j+1, nums.length));
                int sum = nums[i]+nums[j];
                if(numsSet.contains(-sum)){
                    List<Integer> triplet = new ArrayList<>(Arrays.asList(nums[i], nums[j], -sum));
                    Collections.sort(triplet);
                    tripletsSet.add(triplet);
                }
            }
        }
        return new ArrayList<>(tripletsSet);
    }
}
