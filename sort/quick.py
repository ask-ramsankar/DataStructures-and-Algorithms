from sort.utils import SortOrder


# @title Quick Sort Algorithm
# @dev This algorithm follows the Divide and Conquer.
# Step 1: This algorithm chooses the pivot element first (we are using the last element of the list as pivot)
# Step 2: Create partitions based on the pivot value (greater value or lesser values based on the sort order)
# Step 3: Repeat the steps one and two until there are more than one element in the partition
# Time Complexity: O(n * (log n)) [n -> No. of nodes]
class QuickSort:

    def __init__(self, nodes):
        self.nodes = nodes
        self.__nodes = nodes
        self.total_nodes = len(nodes)

    def __partition(self, left_index: int, right_index: int, sort_order: SortOrder) -> int:
        """
        This method sorts the smaller or greater value to the left and right partitions
        based on the pivot value we choose and places the pivot value at the right position of the list
        :param left_index: Left Index of the partition
        :param right_index: Right Index of the partition
        :param sort_order: Order of sorting (Ascending or Descending)
        :return: Index of the pivot value
        """
        
        # Consider the right_index node as current pivot node
        pivot_index = right_index

        # This index will give you the exact position pivot node
        # Initiating it to left_index - 1 because we will increment before every swap
        finder_index = left_index - 1

        for traverse_index in range(left_index, right_index + 1):
            if sort_order == SortOrder.ASC and self.__nodes[traverse_index] < self.__nodes[pivot_index]:
                finder_index += 1
                self.__nodes[traverse_index], self.__nodes[finder_index] = (
                    self.__nodes[finder_index],
                    self.__nodes[traverse_index]
                )

            elif sort_order == SortOrder.DESC and self.__nodes[traverse_index] > self.__nodes[pivot_index]:
                finder_index += 1
                self.__nodes[traverse_index], self.__nodes[finder_index] = (
                    self.__nodes[traverse_index],
                    self.__nodes[traverse_index]
                )

        exact_pivot_index = finder_index + 1
        self.__nodes[exact_pivot_index], self.__nodes[pivot_index] = (
            self.__nodes[pivot_index],
            self.__nodes[exact_pivot_index]
        )
        return exact_pivot_index

    def __quick_sort(self, start_index, end_index, sort_order: SortOrder) -> None:
        """
        This is the helper method of the quick sort to organize the recursive calls.
        It checks the pivot index and split the partitions and continue until
        there are not more than one element in the partition
        :param start_index: Left Index of the partition
        :param end_index: Right Index of the partition
        :param sort_order: Order of sorting (Ascending or Descending)
        """

        if start_index < end_index:
            pivot_index = self.__partition(start_index, end_index, sort_order)

            # Sort and Partitioning Left nodes
            self.__quick_sort(start_index, pivot_index - 1, sort_order)

            # Sort and Partitioning Right nodes
            self.__quick_sort(pivot_index + 1, end_index, sort_order)

    def sort(self, sort_order):
        """
        This method just calls the __quick_sort to sort the nodes
        Kept it separate because of the recursive calls and conditon checks
        :param sort_order: Order of sorting (Ascending or Descending)
        :return: Sorted Nodes list
        """

        self.__quick_sort(0, self.total_nodes - 1, sort_order)
        return self.__nodes


if __name__ == '__main__':
    # Example Use-case
    eg_nodes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    # Insertion Sort
    print("Sorted (Ascending):", QuickSort(eg_nodes).sort(SortOrder.ASC))
    # --> [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    print("Sorted (Descending):", QuickSort(eg_nodes).sort(SortOrder.DESC))
    # --> [44, 42, 35, 33, 31, 27, 26, 19, 14, 10]
