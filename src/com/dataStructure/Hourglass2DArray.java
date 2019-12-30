package dataStructureAlgorithmQuestions;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class Hourglass2DArray {

    /*
     * Hacker Rank Algorithm Question - 2D Array - DS Solution
     *
     * Solved Date : 2019-08-10
     * Author : TK Lee
     *
     * Source : https://www.hackerrank.com/challenges/2d-array/problem
     */

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {

        int r = 0;
        int maxLength = arr.length-1;
        int maxSum = Integer.MIN_VALUE;
        int temp = 0;

        while ((r+2) <= maxLength){
            int c = 0;

            while ((c+2) <= maxLength){

                temp = arr[r][c] + arr[r][(c+1)] + arr[r][(c+2)] + arr[(r+1)][(c+1)] + arr[(r+2)][c] + arr[(r+2)][(c+1)] + arr[(r+2)][(c+2)];
                System.out.println (temp);
                if(temp > maxSum) {
                    maxSum = temp;
                    System.out.println (maxSum);
                }

                c++;
            }

            r++;
        }

        return maxSum;
    }

    private static final Scanner scanner = new Scanner(System.in);

        public static void main(String[] args) throws IOException {

            //Manual Test Code;
            int[][] testArr = {  {1, 1, 1, 0, 0, 0},
                                {0, 1, 0, 0, 0, 0},
                                {1, 1, 1, 0, 0, 0},
                                {0, 0, 2, 4, 4, 0},
                                {0, 0, 0, 2, 0, 0},
                                {0, 0, 2, 2, 4, 0}
                            };

            int[][] testArr2 = {
                    {-1, -1, 0, -9, -2, -2},
                    {-2, -1, -6, -8, -2, -5},
                    {-1, -1, -1, -2, -3, -4},
                    {-1, -9, -2, -4, -4, -5},
                    {-7, -3, -3, -2, -9, -9},
                    {-1, -3, -1, -2, -4, -5}
            };

            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

            int[][] arr = new int[6][6];

            for (int i = 0; i < 6; i++) {
                String[] arrRowItems = scanner.nextLine().split(" ");
                scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

                for (int j = 0; j < 6; j++) {
                    int arrItem = Integer.parseInt(arrRowItems[j]);
                    arr[i][j] = arrItem;
                }
            }

            int result = hourglassSum(arr);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();

            bufferedWriter.close();

            scanner.close();
        }
}