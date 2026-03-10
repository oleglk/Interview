# lc0025__reverse_k_groups.py

# The idea: reverse each group by standard list reversal.
# dummy>1>2>3>4>5>6>0
#       ^
# - temporarily insert break after k nodes; save nextGroup ptr
# dummy>1>2>3>0 nextGroup>4>5>6>0
#       ^
# - reverse null-terminated group of k nodes; obtain pointer to the group's new last element
# dummy>3>2>1>0 nextGroup>4>5>6>0
#           ^
# - connect the group's new last element to nextGroup; next group to reverse = nextGroup
# dummy>3>2>1>4>5>6>0
#             ^
# dummy-head-node.next = head
# elemToConnectGroupTo = dummy-head-node
# nextGroup = head
# while ...:
#   oldGroupHead, oldGroupTail = find_k_group(nextGroup)
#   # (note that oldGroupHead == nextGroup)
#   if (oldGroupHead == oldGroupTail):  break  # no more complete groups
#   nextGroup = oldGroupTail.next
#   oldGroupTail.next = None  # tmp
#   reverse_list(oldGroupHead)
#   elemToConnectGroupTo.next = oldGroupTail
#   elemToConnectGroupTo = oldGroupHead
