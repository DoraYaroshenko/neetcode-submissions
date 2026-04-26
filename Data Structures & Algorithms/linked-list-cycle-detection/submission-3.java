/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode p1 = head;
        ListNode p2 = head;
        if(head==null || head.next==null) return false;
        int index=0;
        while(p2!=null){
            if(p1==p2&&index!=0) return true;
            p1=p1.next;
            p2=p2.next.next;
            index++;
        }
        return false;
    }
}
