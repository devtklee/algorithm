package dataStructureAlgorithmQuestions;

import java.util.Scanner;

public class LeftRotation {

    /*
     * Hacker Rank Algorithm Question - Left Rotation - Solution
     * *
     * Category : Data Structure
     * Solved Date : 2019-08-21
     * Author : TK Lee
     *
     * Source : https://www.hackerrank.com/challenges/array-left-rotation/problem
     */

    public static int[] toTheLeft (int[] arr, int shift){

        int [] shifted = new int [arr.length];
        int cur = 0 ;

        for (int i = arr.length -1 ; i >= 0; i--){

            cur = i - shift ;

            if(cur < 0) {
                cur = arr.length - Math.abs(cur);
            }

            shifted[cur] = arr[i] ;
        }

        return shifted;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] nd = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nd[0]);

        int d = Integer.parseInt(nd[1]);

        int[] a = new int[n];

        String[] aItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int aItem = Integer.parseInt(aItems[i]);
            a[i] = aItem;
        }

        a = toTheLeft(a, d);

        for (int i = 0; i<a.length; i++){
            System.out.print(a[i] + " ");
        }

        scanner.close();
    }

}
