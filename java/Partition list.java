class Solution {
    public ListNode partition(ListNode head, int x) {

        // Dummy nodes for two lists
        ListNode smallDummy = new ListNode(0);
        ListNode largeDummy = new ListNode(0);

        ListNode small = smallDummy;
        ListNode large = largeDummy;

        // Traverse original list
        while (head != null) {

            if (head.val < x) {
                small.next = head;
                small = small.next;
            } else {
                large.next = head;
                large = large.next;
            }

            head = head.next;
        }

        // Connect small list with large list
        small.next = largeDummy.next;

        // Important: terminate the list
        large.next = null;

        return smallDummy.next;
    }
}
