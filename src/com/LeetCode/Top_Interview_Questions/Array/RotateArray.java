package com.LeetCode.Top_Interview_Questions;

public class RotateArray {

    
    public static void rotate (int[] nums, int k){

        int[] rotated = nums.clone();
        int curpos=k;

        for (int idx=0; idx<nums.length; idx++){
            
            curpos++;
            
            if(curpos >= nums.length){
                curpos=0;
            } 
            nums[idx]=rotated[curpos];
        }

        toString(nums);
    }

    public static void toString (int[] nums){
        for(int c=0; c<nums.length; c++){
            System.out.print(nums[c]);
         }
    }

    public static void main (String[] args){

        int[] nums = {1,2,3,4,5,6,7};
        int k = 3;

        int [] nums2 = {-1,-100,3,99};
        int k2=2;
        
         //rotate(nums, k);
         rotate(nums2, k2);
       

    }
    
}
