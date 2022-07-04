from sort.utils import SortOrder


# @title: It is one of the basic sorting algorithm.
# @dev: It traverses through the nodes n times to find the smallest/largest node each time
# Time Complexity: O(n**2) [n -> No. of nodes]
class SelectionSort:

    def __init__(self, nodes):
        self.nodes = nodes
        self.__nodes = nodes
        self.total_nodes = len(nodes)
        assert self.total_nodes > 1, "Not enough nodes to sort"

    def sort(self, sort_order: SortOrder) -> list:
        """
        This method sort the nodes using Selection sort algorithm
        based on the sort order (ascending or descending)
        :param sort_order: 0(ascending) or 1(descending)
        :return: Sorted Nodes List
        """
        for node_index in range(self.total_nodes):
            selected_index = node_index
            for traverse_index in range(node_index + 1, self.total_nodes):

                # To order in ascending order
                if sort_order == SortOrder.ASC and self.__nodes[traverse_index] < self.__nodes[selected_index]:
                    selected_index = traverse_index

                # To order in descending order
                elif sort_order == SortOrder.DESC and self.__nodes[traverse_index] > self.__nodes[selected_index]:
                    selected_index = traverse_index

            # Swapping the selected index with the node's position
            (
                self.__nodes[node_index],
                self.__nodes[selected_index]
            ) = self.__nodes[selected_index], self.__nodes[node_index]
        return self.__nodes


if __name__ == '__main__':
    # Example Use-case
    eg_nodes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    # Selection Sort
    print("Sorted (Ascending):", SelectionSort(eg_nodes).sort(SortOrder.ASC))
    # --> [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    print("Sorted (Descending):", SelectionSort(eg_nodes).sort(SortOrder.DESC))
    # --> [44, 42, 35, 33, 31, 27, 26, 19, 14, 10]
