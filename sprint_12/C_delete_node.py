# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def solution(node, idx):
    if idx == 0:
        new_node = node.next
        return new_node
    previous_node = get_node_by_index(node, idx - 1)
    next_node = get_node_by_index(node, idx)
    previous_node.next = next_node.next
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next is node2
    assert new_head.next.next is node3
    assert new_head.next.next.next is None
    # result is node0 -> node2 -> node3


def test2():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 2)
    assert new_head is node0
    assert new_head.next is node1
    assert new_head.next.next is node3
    assert new_head.next.next.next is None
    # result is node0 -> node1 -> node3


if __name__ == '__main__':
    test()
    test2()
