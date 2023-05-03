from typing import Dict, List, Tuple, Union, Any
import heapq

class PriorityQueue:
    def __init__(self) -> None:
        """
        Initialize a PriorityQueue object.
        """
        self.heap: List[Tuple[int, Any]] = []

    def push(self, item: Any, priority: int) -> None:
        """
        Push an item with a priority value onto the priority queue.

        :param item: The item to push
        :param priority: The priority value of the item
        """
        heapq.heappush(self.heap, (priority, item))

    def pop(self) -> Tuple[int, Any]:
        """
        Pop and return the item with the smallest priority value from the priority queue.

        :return: The item with the smallest priority value
        """
        return heapq.heappop(self.heap)

    def is_empty(self) -> bool:
        """
        Check if the priority queue is empty.

        :return: True if the priority queue is empty, False otherwise
        """
        return len(self.heap) == 0

    def __repr__(self) -> str:
        """
        Return a string representation of the PriorityQueue object.

        :return: A string representation of the PriorityQueue object
        """
        return f"PriorityQueue({self.heap})"


def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start: str, end: str) -> Tuple[int, List[str]]:
    """
    Implementation of Dijkstra's algorithm to find the shortest path between two nodes in a graph.
    
    :param graph: A dictionary representing the graph with nodes as keys and lists of tuples (neighbor, cost) as values
    :param start: The start node
    :param end: The end node
    :return: A tuple (shortest path cost, shortest path) or (-1, []) if no path is found
    """
    pq = PriorityQueue()
    pq.push((start, []), 0)
    visited = set()

    while not pq.is_empty():
        cost, (current, path) = pq.pop()
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]
        if current == end:
            return cost, path
        for neighbor, edge_cost in graph[current]:
            pq.push((neighbor, path), cost + edge_cost)

    return -1, []

def shortest_path(graph: Dict[str, List[Tuple[str, int]]], start: str, end: str) -> Tuple[int, List[str]]:
    """
    Returns the shortest path cost and the shortest path itself from start to end in the given graph using Dijkstra's algorithm.

    :param graph: A dictionary representing the graph with nodes as keys and lists of tuples (neighbor, cost) as values
    :param start: The start node
    :param end: The end node
    :return: A tuple (shortest path cost, shortest path) or (-1, []) if no path is found
    """
    if not graph or start not in graph or end not in graph:
        return -1, []

    return dijkstra(graph, start, end)

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': [('E', 3)],
        'E': []
    }

    cost, path = shortest_path(graph, 'A', 'E')  # Output: (7, ['A', 'B', 'C', 'D', 'E'])
    print(f"Shortest path cost: {cost}\nShortest path: {path}")
