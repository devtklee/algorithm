package dataStructureAlgorithmQuestions;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.Arrays;
import java.util.concurrent.*;
import java.util.regex.*;

public class SparseArrays {

    /*
     * Hacker Rank Algorithm Question - Sparse Array Solution
     *
     * Solved Date : 2019-08-26
     * Author : TK Lee
     *
     * Source : https://www.hackerrank.com/challenges/sparse-arrays/problem
     */


    // Complete the matchingStrings function below.
    static int[] matchingStrings(String[] strings, String[] queries) {

        int [] resultVal = new int [queries.length];

        for (int idx = 0; idx < strings.length; idx++){

            if(idx < queries.length){
                resultVal[idx] = 0;
            }

            if(Arrays.asList(queries).contains(strings[idx])){
               resultVal[Arrays.asList(queries).indexOf(strings[idx])]++;
            }

        }

        return resultVal;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int stringsCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] strings = new String[stringsCount];

        for (int i = 0; i < stringsCount; i++) {
            String stringsItem = scanner.nextLine();
            strings[i] = stringsItem;
        }

        int queriesCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] queries = new String[queriesCount];

        for (int i = 0; i < queriesCount; i++) {
            String queriesItem = scanner.nextLine();
            queries[i] = queriesItem;
        }

        int[] res = matchingStrings(strings, queries);

        for (int i = 0; i < res.length; i++) {
            //bufferedWriter.write(String.valueOf(res[i]));
            System.out.print(res[i]);
            if (i != res.length - 1) {
                //bufferedWriter.write("\n");
                System.out.print("\n");
            }
        }

        //bufferedWriter.newLine();

        //bufferedWriter.close();

        scanner.close();
    }
}
