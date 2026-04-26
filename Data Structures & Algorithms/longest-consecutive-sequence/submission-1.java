class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> startEnd = new HashMap<>();
        HashMap<Integer, Integer> endStart = new HashMap<>();
        for(int num:nums){
            if(startEnd.get(num+1)==null && endStart.get(num-1)==null){
                if(startEnd.get(num)==null && endStart.get(num)==null){
                    startEnd.put(num,num);
                    endStart.put(num,num);
                }
            }
            else if(startEnd.get(num+1)!=null && endStart.get(num-1)==null){
                int end = startEnd.get(num+1);
                startEnd.remove(num+1);
                startEnd.put(num, end);
                endStart.put(end,num);
            }
            else if(startEnd.get(num+1)==null && endStart.get(num-1)!=null){
                int start = endStart.get(num-1);
                endStart.remove(num-1);
                endStart.put(num, start);
                startEnd.put(start,num);
            }
            else{
                int start = endStart.get(num-1);
                int end = startEnd.get(num+1);
                startEnd.put(start, end);
                endStart.put(end, start);
                startEnd.remove(num+1);
                endStart.remove(num-1);
            }
        }
        int maxSec = 0;
        for(int num:startEnd.keySet()){
            if(startEnd.get(num)-num+1>maxSec) maxSec=startEnd.get(num)-num+1;
        }
        return maxSec;
    }
}
