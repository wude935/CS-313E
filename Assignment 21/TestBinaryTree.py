#  File: TestBinaryTree.py

#  Description: Functions with Binary Trees

#  Student's Name: Victor Li

#  Student's UT EID: vql83

#  Partner's Name: Derek Wu

#  Partner's UT EID: dw29924

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 22 November, 2019

#  Date Last Modified: 22 November, 2019


class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree (object):
    def __init__(self):
        self.root = Node(None)
        self.size = 0
        self.height = 0

    # adds a node with value of data
    def add_node(self, data):
        new_node = Node(data)
        current = self.root
        parent = self.root
        if self.size == 0:
            self.root = new_node
        else:
            # traverses the tree until there is current is None
            while current != None:
                parent = current
                if new_node.data <= parent.data:
                    current = current.lchild
                elif new_node.data > parent.data:
                    current = current.rchild
            # adds the new node to left or right of the parent
            if new_node.data <= parent.data:
                parent.lchild = new_node
            elif new_node.data > parent.data:
                parent.rchild = new_node
        self.size += 1
        self.search_and_get_height(self.root, 0)

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        # if the size of the trees are different, return False
        if self.size != pNode.size:
            return False
        else:
            return self.search_and_compare(self.root, pNode.root)

    # recursively searchs the nodes of both trees and compares the values
    def search_and_compare(self, current_self, current_pNode):
        # if the nodes are not the same, return False
        if current_self != None or current_pNode != None:
            if current_self.data != current_pNode.data:
                return False
            else:
                self.search_and_compare(
                    current_self.lchild, current_pNode.lchild)
                self.search_and_compare(
                    current_self.rchild, current_pNode.rchild)
                return True

    # Prints out all nodes at the given level
    def print_level(self, level):
        if self.size == 0:
            return None
        else:
            self.search_and_print(self.root, level, 0)

    # recursively searches the tree and prints out all numbers on a certain level
    def search_and_print(self, node, target_level, current_level):
        if node == None:
            return
        elif target_level == current_level:
            print(node.data)
        else:
            self.search_and_print(node.lchild, target_level, current_level + 1)
            self.search_and_print(node.rchild, target_level, current_level + 1)

    # Returns the height of the tree

    def get_height(self):
        return self.height

    def search_and_get_height(self, node, current_height):
        if node == None:
            return
        elif node != None:
            if current_height > self.height:
                self.height = current_height
                self.search_and_get_height(node.lchild, current_height + 1)
                self.search_and_get_height(node.rchild, current_height + 1)
            else:
                self.search_and_get_height(node.lchild, current_height + 1)
                self.search_and_get_height(node.rchild, current_height + 1)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        if self.size == 0:
            return 0
        else:
            return self.search_and_get_num_nodes(self.root)

    def search_and_get_num_nodes(self, node):
        if node == None:
            return 0
        else:
            return self.search_and_get_num_nodes(node.lchild) + self.search_and_get_num_nodes(node.rchild) + 1


def main():
    # Create three trees - two are the same and the third is different
    same_tree_1 = Tree()
    same_tree_2 = Tree()
    different_tree = Tree()
    same_tree_list = [4, 6, 3, 1, 5, 2, 0, -1]
    different_tree_list = [5, 6, 1, 0, 4]
    for num in same_tree_list:
        same_tree_1.add_node(num)
        same_tree_2.add_node(num)
    for num in different_tree_list:
        different_tree.add_node(num)
    # Test your method is_similar()
    print('Testing is_similar():')
    print(same_tree_1.is_similar(different_tree))
    # Print the various levels of two of the trees that are different
    print('Testing print_level() with same_tree_1:')
    same_tree_1.print_level(2)
    print('Testing print_level() with different_tree:')
    different_tree.print_level(1)
    # Get the height of the two trees that are different
    print('Testing get_height() with same_tree_1:')
    print(same_tree_1.get_height())
    print('Testing get_height() with different_tree')
    print(different_tree.get_height())
    # Get the total number of nodes a binary search tree
    print('Testing num_nodes() with same_tree_1:')
    print(same_tree_1.num_nodes())


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
