package com.HackerRank;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class SockMerchant {
    /*
     * Hacker Rank Algorithm Question - Sock Merchant
     * *
     * Category : Warm-up Challenges
     * Solved Date : 2019-12-29
     * Author : TK Lee
     *
     * Source : https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
     */

    // Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {

        int paircnt =0;
        Map<Integer,Integer> pile = new HashMap<Integer, Integer>();

        for(int idx =0; idx<n; idx++)
        {
            if (pile.containsKey(ar[idx])){
                pile.replace(ar[idx], (pile.get(ar[idx])+1));

            } else {
                pile.put(ar[idx],1);
            }
        }

        for (Map.Entry<Integer, Integer> entry : pile.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if (value > 1) {
                paircnt += (value / 2);
            }
        }
        return paircnt;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {

        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] ar = new int[n];

        String[] arItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arItem = Integer.parseInt(arItems[i]);
            ar[i] = arItem;
        }

        int result = sockMerchant(n, ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();

    }
}
