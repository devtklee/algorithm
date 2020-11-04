package com.LeetCode;

public class ConsecutiveCharacters {
    /*

    Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
    Return the power of the string.

    Example 1:
    Input: s = "leetcode"
    Output: 2
    Explanation: The substring "ee" is of length 2 with the character 'e' only.

    Example 2:
    Input: s = "abbcccddddeeeeedcba"
    Output: 5
    Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

    Example 3:
    Input: s = "triplepillooooow"
    Output: 5

    Example 4:
    Input: s = "hooraaaaaaaaaaay"
    Output: 11

    Example 5:
    Input: s = "tourist"
    Output: 1


    Constraints:
    1 <= s.length <= 500
    s contains only lowercase English letters.
     */

    public static int maxPower(String s) {

        int cnt=0;
        int tmp=1;
        char cursor = ' ';

        for (int idx=0; idx <= s.length()-1; idx++){

            if(cursor==s.charAt(idx)){
                tmp++;
            } else {
                //if character doesn't match, reset count.
                tmp=1;
            }

            //Find the Maximum count
            if(tmp>=cnt) {
                cnt = tmp;
            }

            //Move Cursor
            cursor = s.charAt(idx);

        }

        return cnt;
    }

    public static void main(String[] args){

    String test1 = "leetcode";
    String test2 = "abbcccddddeeeeedcba";
    String test3 = "triplepillooooow";

    System.out.println(maxPower(test3));

    }
}
