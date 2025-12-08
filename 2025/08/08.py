# for each box, create dict entry for adj list

# how do we find x pairs by euclidean distance?
# calculate all possible pairs: O(n^2)
# sort pairs by distance, O(n^2log(n^2)), take first 1000

# multiply the sizes of three largest circuits

import numpy as np
import itertools
from collections import deque
import math

class Day8:
    def __init__(self, doc: str):
        self.boxes = [tuple(int(dimension) for dimension in line.split(',')) for line in doc.split('\n')]
        # print(self.boxes)
        self.network = {box: [] for box in self.boxes}
        # print(self.network)

    def get_closest_pairs(self, closest_x: int = None):
        # generate all possible pairs, with their distances
        pairs = list(itertools.combinations(self.boxes, 2))
        sorted_pairs = sorted(pairs, key=lambda x : np.linalg.norm(np.array(x[0])-np.array(x[-1])))

        if closest_x is None:
            return sorted_pairs

        return sorted_pairs[:closest_x]
    
    def part1(self, closest_x: int):
        closest_pairs = self.get_closest_pairs(closest_x)
        circuit_sizes = {}
        for (p1, p2) in closest_pairs:
            self.network[p1].append(p2)
            self.network[p2].append(p1)

        # print(self.network)

        # DFS starting from each node in the network, adding all visited nodes to visited
        # if node alr visited, then don't visit it again
        # if node not alr visited, then DFS on it, keep track of number of edges to determine size of circuit
        visited = set()
        for box in self.network:
            if box not in visited:
                size = 0
                stack = deque()
                stack.append(box)
                # print(stack)

                while stack:
                    curr = stack.pop()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    size += 1
                    # print(curr)
                    # print(size)

                    # explore its neighbors
                    for neighbor in self.network[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)

                if size not in circuit_sizes:
                    circuit_sizes[size] = 0
                circuit_sizes[size] += 1
        
        # print(circuit_sizes)
        return math.prod(sorted(circuit_sizes, reverse=True)[:3])


    def part2(self):
        # junction boxes all in the same circuit
        # this means that if you dfs from any node, you should in theory hit all nodes
        num_boxes = len(self.boxes)
        pairs = self.get_closest_pairs()
        for (p1, p2) in pairs:
            self.network[p1].append(p2)
            self.network[p2].append(p1)

            visited = set()
            stack = deque()
            stack.append(self.boxes[0])

            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)

                # explore its neighbors
                for neighbor in self.network[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            if len(visited) == num_boxes:
                return p1[0] * p2[0]


def main():
    with open('08.txt') as f:
        doc = f.read()
    print(f"Part 1: {Day8(doc).part1(1000)}")
    print(f"Part 2: {Day8(doc).part2()}")


if __name__=="__main__":
    main()