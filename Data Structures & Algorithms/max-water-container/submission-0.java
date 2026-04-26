class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length-1;
        HashSet<Integer> amounts = new HashSet<>();
        while(left<right){
            amounts.add(Math.min(heights[left],heights[right])*(right-left));
            if(heights[left]<heights[right]) left++;
            else right--;
        }
        return Collections.max(amounts);
    }
}
