package com.LeetCode.Top_Interview_Questions.Array;

import java.util.Arrays;

public class ContainsDuplicates {

        public static boolean containsDuplicate(int[] nums) {
            
            int pos=1;
            for (int idx=0; idx<nums.length-1; idx++){
                Arrays.sort(nums);
                if(nums[pos]==nums[idx]){
                    return true;
                }
                pos++;
            }
            
            return false;
            
        }    

        public static void main (String[] args){
            
            int[] nums = {1,2,3,4};
            System.out.println(containsDuplicate(nums));
        }
}
