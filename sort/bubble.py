from sort.utils import SortOrder


# @title: Bubble Sort Algorithm
# @notice: This is one of the simplest and basic soring algorithm
# @dev: It repeatedly swaps the adjacent node if it is in wrong order base on ascending or descending
# Time Complexity: O(n**2) [n -> No. of nodes]
class BubbleSort:

    def __init__(self, nodes):
        self.nodes = nodes
        self.__nodes = nodes
        self.total_nodes = len(nodes)
        assert self.total_nodes > 1, "Not enough nodes to sort"

    def sort(self, sort_order: SortOrder) -> list:
        """
        This method sorts the nodes using the Bubble sorting algorithm
        based on sort order (ascending or descending)
        :param sort_order: Order of sorting. 0(ascending) or 1(descending)
        :return: Sorted List of Nodes
        """
        for node_index in range(self.total_nodes):
            swapped = False

            # Note: (self.total_nodes - node_index - 1) -> Is used as upper bound of second loop
            # Because when each iteration completes the largest or the smallest will be moved to the end
            for traverse_index in range(self.total_nodes - node_index - 1):
                adjacent_index = traverse_index + 1
                do_swap = False
                if sort_order == SortOrder.ASC and self.__nodes[traverse_index] > self.__nodes[adjacent_index]:
                    do_swap = True
                elif sort_order == SortOrder.DESC and self.__nodes[traverse_index] < self.__nodes[adjacent_index]:
                    do_swap = True

                if do_swap:
                    (
                        self.__nodes[traverse_index],
                        self.__nodes[adjacent_index]
                    ) = self.__nodes[adjacent_index], self.__nodes[traverse_index]
                    swapped = True
            else:
                if not swapped:
                    # If no swap happened in the inner loop
                    # means all the nodes were already in sorted order
                    break
        return self.__nodes


if __name__ == '__main__':
    # Example Use-case
    eg_nodes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    # Bubble Sort
    print("Sorted (Ascending):", BubbleSort(eg_nodes).sort(SortOrder.ASC))
    # --> [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    print("Sorted (Descending):", BubbleSort(eg_nodes).sort(SortOrder.DESC))
    # --> [44, 42, 35, 33, 31, 27, 26, 19, 14, 10]
