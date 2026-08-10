class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            if l1:
                curr.next = l1
            else:
                curr.next = l2

            return dummy.next

        result = None

        for l in lists:
            result = merge(result, l)

        return result