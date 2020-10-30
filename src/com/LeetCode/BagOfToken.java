package com.LeetCode;


import java.util.Arrays;

public class BagOfToken {

    /*

    LeetCode Algorithm Question - Bag of Tokens Solution
    Solved Date : 2020-10-25
    Author : TK Lee

    Source : https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3506/

    Question Description :

    You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

    Your goal is to maximize your total score by potentially playing each token in one of two ways:

    If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
    If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
    Each token may be played at most once and in any order. You do not have to play all the tokens.

    Return the largest possible score you can achieve after playing any number of tokens.
     */

        public static int bagOfTokensScore(int[] tokens, int P)
        {
            //Variable Initialization
            int[] tokenList = tokens.clone();
            int power = P;
            int maxScore = 0;
            int score = 0;
            int curPower = power;
            int left = 0;
            int right = tokenList.length -1;

            //Array Token List
            Arrays.sort(tokenList);

            while (right >= left) {

                //If Power >= Token, subtract token amount from power to again score.
                if (curPower >= tokenList[left]){
                    score++;
                    curPower -= tokenList[left++];

                    //Keep Maximized scores
                    maxScore = Math.max(maxScore, score);

                } else if (score >0)  {
                    score--;
                    curPower += tokenList[right--];

                } else {
                    return maxScore;
                }
            } ;

            return maxScore;
        }

        public static void main(String[] args){

            int[] tokens = {81,91,31};
            int p = 73;
            int score = 0;

            score = bagOfTokensScore(tokens, p);

            System.out.println("Score: " + score);

        }
    }

