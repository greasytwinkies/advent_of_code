# sort intervals first - n (log n)
# use a stack to resolve overlapping intervals - n
# for each available id, binary search on intervals - k (log n)
# time complexity: (k+n) (log n)
from collections import deque
import re

INTERVAL_PATTERN = re.compile(r'(\d+)-(\d+)', re.MULTILINE)

class Day5:
    def __init__(self, doc: str):
        [intervals, available_ids] = doc.split('\n\n')
        self.intervals = [[int(match[0]), int(match[-1])] for match in re.findall(INTERVAL_PATTERN, intervals)]
        self.available_ids = list(map(int, available_ids.split('\n')))
        # sort intervals
        self.intervals.sort()
        # use an empty stack to sort intervals
        stack = deque()
        for interval in self.intervals:
            start, end = interval[0], interval[-1]
            if not stack:
                stack.append(interval)
            # if stack alr has elements, check that the incoming element does not overlap with any of the previous elements
            # since stack is already sorted by interval start time, only possible overlap is if start time of incoming element >= last element in stack
            # then take the maximum end value of either interval as the new interval
            else:
                # peek the last element of stack
                while stack:
                    last_start, last_end = stack[-1][0], stack[-1][-1]
                    if last_start <= start <= last_end:
                        # pop the last element of stack and update start and end
                        # only append after all iterations
                        stack.pop()
                        start = min(start, last_start)
                        end = max(end, last_end)
                    else:
                        break
                stack.append([start, end])
            
            self.intervals = list(stack)
        # print(self.intervals)
        # print(self.available_ids)
        self.num_intervals = len(self.intervals)
    def is_id_fresh(self, available_id: int):
        low = 0
        high = self.num_intervals-1

        while low <= high:
            mid = (low + high) // 2 
            l, r = self.intervals[mid]

            if available_id < l:
                high = mid-1
            elif available_id > r:
                low = mid+1
            else: # available id is in between start and end of interval
                return True
        
        return False
    
    def part1(self):
        fresh = 0
        for available_id in self.available_ids:
            if self.is_id_fresh(available_id):
                fresh += 1

        return fresh
    
    def part2(self):
        total = 0
        # calculate total number of fresh ingredient IDs
        for interval in self.intervals:
            total += interval[-1] - interval[0] + 1

        return total

def main():
    with open('05.txt') as f:
        doc = f.read()
    print(f'Part 1: {Day5(doc).part1()}')
    print(f'Part 2: {Day5(doc).part2()}')

if __name__=="__main__":
    main()
