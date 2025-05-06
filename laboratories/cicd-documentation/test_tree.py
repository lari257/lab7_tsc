import pytest
from tree import Tree
from node import Node

def test_find_existing_node():
    tree = Tree()
    values = [10, 5, 15]
    for v in values:
        tree.add(v)

    node = tree.find(5)
    assert node is not None
    assert node.data == 5

def test_find_nonexistent_node():
    tree = Tree()
    values = [10, 5, 15]
    for v in values:
        tree.add(v)

    node = tree.find(7)
    assert node is None
