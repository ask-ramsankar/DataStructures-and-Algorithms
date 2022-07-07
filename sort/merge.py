from sort.utils import SortOrder


# @title Merge Sorting
# @notice This is once of the sorting algorithm which time complexity is lesser
# when compared to the linear sorting algorithms (Selection, Bubble, etc)
# @dev This algo follows the Divide and Conquer method. It divides the nodes upto single node
# then sorts by combining it
# Time Complexity: O(n * log (n)) [n -> No. of nodes]
class MergeSort:

    def __init__(self, nodes):
        self.nodes = nodes
        self.__nodes = nodes
        self.total_nodes = len(nodes)
        assert self.total_nodes > 1, "Not enough nodes to sort"

    def __merge_sort(self, _nodes: list, sort_order: SortOrder) -> list:
        """
        Helper internal method to merge and sort the divided nodes
        by following the Merge sort algorithm
        :param _nodes: List of nodes to sort
        :param sort_order: Order of sorting. 0(ascending) or 1(descending)
        :return: List of sorted nodes
        """
        _total_nodes = len(_nodes)
        if _total_nodes <= 1:
            return _nodes

        mid_index = _total_nodes // 2

        left_nodes = _nodes[:mid_index]
        left_nodes = self.__merge_sort(left_nodes, sort_order)

        right_nodes = _nodes[mid_index:]
        right_nodes = self.__merge_sort(right_nodes, sort_order)

        node_index, left_node_index, right_node_index = 0, 0, 0

        # Sorting by comparing the left and right half nodes
        while left_node_index < len(left_nodes) and right_node_index < len(right_nodes):
            if left_nodes[left_node_index] < right_nodes[right_node_index]:
                if sort_order == SortOrder.ASC:
                    _nodes[node_index] = left_nodes[left_node_index]
                    left_node_index += 1
                else:
                    _nodes[node_index] = right_nodes[right_node_index]
                    right_node_index += 1
            else:
                if sort_order == SortOrder.ASC:
                    _nodes[node_index] = right_nodes[right_node_index]
                    right_node_index += 1
                else:
                    _nodes[node_index] = left_nodes[left_node_index]
                    left_node_index += 1
            node_index += 1

        # When the split nodes are not equal, some nodes in either left or right half
        # will not be added is correct order to the _nodes because of the above while condition
        # So we need to update it by checking the index

        # Checking and Updating the left unordered nodes
        while left_node_index < len(left_nodes):
            _nodes[node_index] = left_nodes[left_node_index]
            left_node_index += 1
            node_index += 1

        # Checking  and Updating the right unordered nodes
        while right_node_index < len(right_nodes):
            _nodes[node_index] = right_nodes[right_node_index]
            right_node_index += 1
            node_index += 1

        return _nodes

    def sort(self, sort_order: SortOrder) -> list:
        """
        This method sorts the nodes using the Merge sorting algorithm
        based on sort order (ascending or descending)
        :param sort_order: Order of sorting. 0(ascending) or 1(descending)
        :return: Sorted List of Nodes
        """
        return self.__merge_sort(self.__nodes, sort_order)


if __name__ == '__main__':
    # Example Use-case
    eg_nodes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    # Merge Sort
    print("Sorted (Ascending):", MergeSort(eg_nodes).sort(SortOrder.ASC))
    # --> [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    print("Sorted (Descending):", MergeSort(eg_nodes).sort(SortOrder.DESC))
    # --> [44, 42, 35, 33, 31, 27, 26, 19, 14, 10]
