from heap_ds.heap_type import HeapType
from sort.utils import SortOrder


# Heap Data Structure
# @note: Heap is a binary tree following few properties
# |-- 1. Complete tree (other than the last level each level should be completely filled).
# |----  This property makes it suitable to store the Heap in the list
# |-- 2. Parent node of each child is lesser in Min-Heap and greater in Max-Heap
# |-- 3. Time Complexity: O(n * log(n)) [n -> No. of nodes]
# @dev: Each state of the heap while structuring will be stored in self.__heap
class Heap:

    def __init__(self, nodes: list):
        self.total_nodes = len(nodes)
        assert self.total_nodes > 1, "Heap should contains 2 nodes at least"

        self.nodes = nodes
        self.__heap = list()

    @staticmethod
    def get_parent_index(index: int) -> int:
        """
        (Formula) Used to get the parent node's index of the current index
        :param index: current node's index
        :return: parent node's index
        """
        return (index - 1) // 2

    @staticmethod
    def get_left_index(index: int) -> int:
        """
        (Formula) Used to get the left child node's index of the current index
        :param index: current node's index
        :return: left child node's index
        """
        return (index * 2) + 1

    @staticmethod
    def get_right_index(index: int) -> int:
        """
        (Formula) Used to get the right child node's index of the current index
        :param index: current node's index
        :return: right child node's index
        """
        return (index * 2) + 2

    def __heapify(self, heap_type: HeapType, heap_size: int, index: int):
        """
        Internal method to arrange the heap structure using the current index
        and stores the data in internal __heap list
        :param heap_type: MIN or MAX
        :param heap_size: Size of the heap (self.__heap)
        :param index: index of the currently checking node
        """
        left_index = self.get_left_index(index)
        right_index = self.get_right_index(index)

        if heap_type == HeapType.MIN:
            if left_index < heap_size and self.__heap[left_index] < self.__heap[index]:
                self.__heap[left_index], self.__heap[index] = self.__heap[index], self.__heap[left_index]
                self.__heapify(heap_type, heap_size, left_index)

            if right_index < heap_size and self.__heap[right_index] < self.__heap[index]:
                self.__heap[right_index], self.__heap[index] = self.__heap[index], self.__heap[right_index]
                self.__heapify(heap_type, heap_size, right_index)

        elif heap_type == HeapType.MAX:
            if left_index < heap_size and self.__heap[left_index] > self.__heap[index]:
                self.__heap[left_index], self.__heap[index] = self.__heap[index], self.__heap[left_index]
                self.__heapify(heap_type, heap_size, left_index)

            if right_index < heap_size and self.__heap[right_index] > self.__heap[index]:
                self.__heap[right_index], self.__heap[index] = self.__heap[index], self.__heap[right_index]
                self.__heapify(heap_type, heap_size, right_index)

        else:
            raise TypeError("Invalid heap type. Should be 0(MIN) or 1(MAX)")

    def heapify(self, heap_type: HeapType) -> list:
        """
        This method surf through the nodes to form a structured heap
        :param heap_type: Enum: HeapType(MIN, MAX)
        :return: Structured Min/Max heap
        """
        self.__heap = self.nodes.copy()
        for node_index in range(self.total_nodes // 2 - 1, -1, -1):
            if heap_type == HeapType.MIN:
                self.__heapify(heap_type, self.total_nodes, node_index)
            else:
                self.__heapify(heap_type, self.total_nodes, node_index)

        heap = self.__heap
        # Clean-Up
        self.__heap = list()
        return heap

    def sort(self, sort_order: SortOrder):
        """
        Helps to sort the structured heap using
        :param sort_order:
        :return:
        """
        heap_type = HeapType.MIN if sort_order == SortOrder.ASC else HeapType.MAX
        self.__heap = self.heapify(heap_type)

        sorted_heap = list()
        last_node = self.total_nodes - 1
        while last_node >= 0:
            sorted_heap.append(self.__heap[0])
            self.__heap[0] = self.__heap[last_node]
            del self.__heap[last_node]
            last_node -= 1
            heap_size = last_node + 1
            self.__heapify(heap_type, heap_size, 0)

        # Clean-Up
        self.__heap = list()
        return sorted_heap


if __name__ == '__main__':
    # Example Use-case
    eg_nodes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    # Heapify the Nodes
    print("Min Heap:", Heap(eg_nodes).heapify(HeapType.MIN))    # --> [10, 14, 19, 33, 26, 42, 27, 44, 35, 31]
    print("Max Heap:", Heap(eg_nodes).heapify(HeapType.MAX))    # --> [44, 35, 42, 33, 31, 19, 27, 10, 26, 14]
    # Heap Sort
    print("Sorted Heap (Ascending):", Heap(eg_nodes).sort(SortOrder.ASC))
    # --> [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    print("Sorted Heap (Descending):", Heap(eg_nodes).sort(SortOrder.DESC))
    # --> [44, 42, 35, 33, 31, 27, 26, 19, 14, 10]
