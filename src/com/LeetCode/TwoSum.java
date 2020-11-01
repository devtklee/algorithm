package com.LeetCode;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    /*

    LeetCode Algorithm Question - Two Sum Solution
    Solved Date : 2020-10-31
    Author : TK Lee

    Source : https://leetcode.com/problems/two-sum/

    Question Description :
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    */

    public static int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> numbers = new HashMap<Integer, Integer>();
        int[] sum = {0, 0};
        int n =0;

        for (int idx=0; idx<nums.length; idx++){

            n=target-nums[idx];

           if (numbers.containsKey(n)){

               sum[0] = idx;
               sum[1] = numbers.get(n);

           } else {
               numbers.put(nums[idx], idx);
           }
        }

         Arrays.sort(sum);
        return sum;

    }

    public static void main (String[] args) {

        int[] numSet1 = {3,2,4};
        int[] result = new int [2];

        result=twoSum(numSet1, 6);
        System.out.println (result[0]+ ", "  + result[1]);

    }

}
