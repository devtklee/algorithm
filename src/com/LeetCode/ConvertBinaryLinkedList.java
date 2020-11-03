package com.LeetCode;

public class ConvertBinaryLinkedList {

    /*

    LeetCode Algorithm Question - Convert Binary Number in a Linked List to Integer Solution
    Solved Date : 2020-11-02
    Author : TK Lee

    Source : https://leetcode.com/explore/featured/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3516/
    Question Description :
    Convert Binary Number in a Linked List to Integer
    Given head which is a reference node to a singly-linked list.
    The value of each node in the linked list is either 0 or 1.
    The linked list holds the binary representation of a number.

    Return the decimal value of the number in the linked list.

    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10

    */

    /**
     * Definition for singly-linked list.
     */
      public static class ListNode {
          int val;
          ListNode next;
          ListNode() {}
          ListNode(int val) { this.val = val; }
          ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     }


    public static int getDecimalValue(ListNode head) {

            ListNode currentNode = head;
            StringBuffer binaryNum = new StringBuffer();
            int decNum = 0;

            binaryNum.append(head.val);

            while(currentNode.next != null){

              binaryNum.append(currentNode.next.val);
              currentNode = currentNode.next;

            }
            System.out.println ("Converting Binary : " + binaryNum.toString());
            //Back Cursor
            int pow = binaryNum.length()-1;
            int multiple = 0;

            //Convert Bin to DEC
            for (int idx = 0; idx <= binaryNum.length()-1; idx++){

            System.out.println("idx : " + idx);
            System.out.println("pow : " + pow );

            if (pow == 0){
                //For the 2^0, return 1
                multiple = 1;
            } else {
                multiple = (int)Math.pow(2, pow);
            }

            decNum += Integer.parseInt(binaryNum.charAt(idx) + "") * multiple;

            //Move Cursor
            pow--;
        }
        return decNum;
    }

    public static void main (String[] args){

        ListNode ln14 = new ListNode(0);
        ListNode ln13 = new ListNode(0, ln14);
        ListNode ln12 = new ListNode(0, ln13);
        ListNode ln11 = new ListNode(0, ln12);
        ListNode ln10 = new ListNode(0, ln11);
        ListNode ln9 = new ListNode(0, ln10);
        ListNode ln8 = new ListNode(1, ln9);
        ListNode ln7 = new ListNode(1, ln8);
        ListNode ln6 = new ListNode(1, ln7);
        ListNode ln5 = new ListNode(0, ln6);
        ListNode ln4 = new ListNode(0, ln5);
        ListNode ln3 = new ListNode(1, ln4);
        ListNode ln2 = new ListNode(0, ln3);
        ListNode ln1 = new ListNode(0, ln2);
        ListNode ln = new ListNode(1, ln1);


        int num=0;
        num = getDecimalValue(ln);
       System.out.println (num);

    }
}
