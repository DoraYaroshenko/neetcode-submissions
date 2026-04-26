class Solution {
    public int maxProfit(int[] prices) {
        int max = prices[prices.length-1];
        int profit = 0;
        for(int i=prices.length-2;i>=0;i--){
            if(max-prices[i]>profit){
                profit=max-prices[i];
            }
            if(prices[i]>max){
                max = prices[i];
            }
        }
        return profit;
    }
}
