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



    public static int bagOfTokensScore(int[] tokens, int p)
    {
        //Variable Initialization
        int[] tokenList = tokens.clone();
        int power = p;
        int score = 0;
        int curPower = power;
        int tmp =0;
        int left = 0;
        int right = tokenList.length -1;

        //Sort Array List
        for (int idx=0; idx < tokenList.length; idx++ ) {
            for (int next_idx=idx; next_idx < tokenList.length; next_idx++)
            {
                if (tokenList[idx] >= tokenList[next_idx]) {
                    tmp = tokenList[idx];
                    tokenList[idx] = tokenList[next_idx];
                    tokenList[next_idx] = tmp;
                }
            }
        }

        while (right != left) {

            System.out.println ("Current Pointer : ");
            System.out.println("Right : " + right);
            System.out.println("Left : " + left + "\n");

            //If Power is less then any of token, return current score;
            if (tokenList[left] > curPower && (tokenList[right]) < curPower){
                return score;
            }

            //Face Up
            if (tokenList[left] <= curPower){
                score++;
                curPower -= tokenList[left];
                left++;

                print("UP", score, curPower);
            } else if ((tokenList[right]) >= curPower && score >0) {
                score--;
                curPower += tokenList[right];
                right--;

                print("DOWN", score, curPower);

            }

        } ;

        return score;
    }

    static void print(String pt, int s, int p){
        System.out.println("Move : " + pt);
        System.out.println("Score : " + s);
        System.out.println("Power : " + p);
        System.out.println("");
    }


    public static void main(String[] args){

        int[] tokens = {100,200,300,400};
        int p = 200;
        int score = 0;

        score = bagOfTokensScore(tokens, p);

        System.out.println(score);

    }
}

