package com.HackerRank;

import java.util.Scanner;

public class DiagonalDifference {

    /*
     * Hacker Rank Algorithm Question - Diagonal Difference Solution
     *
     * Solved Date : 2019-07-25
     * Author : TK Lee
     *
     * Source : https://www.hackerrank.com/challenges/diagonal-difference/problem
     */

    public static void main (String[] args){

        int left = 0;
        int right = 0;
        int val = 0;
        Scanner sc = new Scanner(System.in);
        
        int rowNum = sc.nextInt();

        //Test Cases
        //int[][] matrix =  {{11, 2, 4}, {4,5,6}, {10, 8, -12}};

        for (int row = 0 ; row<rowNum; row++){
            for(int col = 0; col<rowNum; col++){

              val = sc.nextInt();
              // val = matrix[row][col];
               
               if(row == col){
                    left += val;
                }
               if(col == rowNum - (1 + row)){
                    right += val;
                }
            }
        }

        System.out.println (Math.abs(left - right));
    }
}
