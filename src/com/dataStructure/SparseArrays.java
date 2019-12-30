package dataStructureAlgorithmQuestions;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Arrays;

public class SparseArrays {

    // Complete the matchingStrings function below.
    static int[] matchingStrings(String[] strings, String[] queries) {

        int [] resultVal = new int [queries.length];
        Map<String, Integer> stringMap = new HashMap<String, Integer>();

        for (int sidx = 0; sidx < strings.length; sidx++){

            /*
            Doesn't work with string array with duplicated string.
            //indexOf method only return first match
            if(Arrays.asList(queries).indexOf(strings[idx]) != -1){
                resultVal[Arrays.asList(queries).indexOf(strings[idx])]++;
            }
            */

            /* This solution is O(n^2)
            for (int qidx = 0; qidx < queries.length; qidx++){

                if(strings[sidx].equals(queries[qidx])){
                    resultVal[qidx] += 1;
                }
            }
            */

            if (stringMap.containsKey(strings[sidx])){
                stringMap.put(strings[sidx], stringMap.get(strings[sidx])+1 );
            } else {
                stringMap.put(strings[sidx], 1);
            }
        }


        for( int i = 0; i <queries.length; i++){

            if(stringMap.containsKey(queries[i])){
                resultVal[i] = stringMap.get(queries[i]);
            } else {
                resultVal[i] = 0;
            }

        }


        return resultVal;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

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
            bufferedWriter.write(String.valueOf(res[i]));

            if (i != res.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }

}
