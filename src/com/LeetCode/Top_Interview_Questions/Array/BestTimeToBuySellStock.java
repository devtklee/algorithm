package com.LeetCode.Top_Interview_Questions.Array;

public class BestTimeToBuySellStock {

    public static int getMaxProfit (int[] prices){
        
        int profit = 0;

        for(int i=1; i<prices.length; i++){

            int diff = prices[i]-prices[i-1];
            
            if(diff > 0){
                profit += diff;
            }
        }

        return profit;
    }

    public static void main (String[] args){
        
        int[] prices = {7,1,5,3,6,4};

        System.out.println(getMaxProfit(prices));

    }
    
}
