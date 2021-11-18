package com.LeetCode.Top_Interview_Questions.Array;

public class RemoveDuplicatesFromSortedArray{

    public int main (int[] nums){
       
        int k = 0;
        
        //Count duplicates
        for (int i=1; i<nums.length; i++){
            if(nums[k]!=nums[i]){
                k++;
                nums[k]=nums[i];
            }    
        }
        
        //Return latest duplicates
        return ++k;
    }
}