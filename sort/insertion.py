from sort.utils import SortOrder


# @title Insertion Sorting
# @notice This sorting algorithm simply sort the nodes as we arrange the card.
# @dev By continuously checking the prev adjacent node and swapping the unordered
# Time Complexity: O(n**2) [n -> No. of nodes]
class InsertionSort:

    def __init__(self, nodes):
        self.nodes = nodes
        self.__nodes = nodes
        self.total_nodes = len(nodes)
        assert self.total_nodes > 1, "Not enough nodes to sort"

    def sort(self, sort_order: SortOrder) -> list:
        """
        This method sorts the nodes using the Insertion sorting algorithm
        based on sort order (ascending or descending)
        :param sort_order: Order of sorting. 0(ascending) or 1(descending)
        :return: Sorted List of Nodes
        """
        for node_index in range(1, self.total_nodes):
            current_index = node_index
            adjacent_index = node_index - 1
            while adjacent_index >= 0:
                do_swap = False
                if sort_order == SortOrder.ASC and self.__nodes[current_index] < self.__nodes[adjacent_index]:
                    do_swap = True
                if sort_order == SortOrder.DESC and self.__nodes[current_index] > self.__nodes[adjacent_index]:
                    do_swap = True

                if do_swap:
                    (
                        self.__nodes[adjacent_index],
                        self.__nodes[current_index]
                    ) = self.__nodes[current_index], self.__nodes[adjacent_index]
                    current_index -= 1
                    adjacent_index -= 1
                else:
                    break
        return self.__nodes


if __name__ == '__main__':
    # Example Use-case
    eg_nodes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    # Bubble Sort
    print("Sorted (Ascending):", InsertionSort(eg_nodes).sort(SortOrder.ASC))
    # --> [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    print("Sorted (Descending):", InsertionSort(eg_nodes).sort(SortOrder.DESC))
    # --> [44, 42, 35, 33, 31, 27, 26, 19, 14, 10]
