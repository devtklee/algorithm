package com.LeetCode.Top_Interview_Questions.Array;

public class RotateArray {

    
    public static void rotate (int[] nums, int k){

        int[] rot = nums.clone();
        int pos=k;
        int numSize = nums.length;
        
        for (int j=0; j<numSize; j++){
            
            pos=k+j;
            
            if(pos>=numSize){
                pos=Math.abs(numSize-pos);
            }
            nums[pos]=rot[j];
        }

        toString(nums);
    }

    public static void toString (int[] nums){
        System.out.print("\n[");
        for(int c=0; c<nums.length; c++){
            System.out.print(nums[c]+ " ") ;
         }
         System.out.print("]\n");
    }

    public static void main (String[] args){

        int[] nums = {1,2,3,4,5,6,7};
        int k = 3;

        int [] nums2 = {-1,-100,3,99};
        int k2=2;
        
        toString(nums2);
         //rotate(nums, k);
         rotate(nums2, k2);
       

    }
    
}
