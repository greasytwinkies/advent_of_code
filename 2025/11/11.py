# dfs from you, terminating at out
from functools import lru_cache
class Day11:
    def __init__(self, cables: dict):
        self.cables = cables
    
    @lru_cache(None)
    def count_paths(self, node, end):
        """Count number of ways to go from node → end."""
        if node == end:
            return 1

        total = 0
        for nxt in self.cables.get(node, []):
            total += self.count_paths(nxt, end)
        return total
                

    # def count_paths(self, start: str, end: str):
    #     stack = deque()
    #     # add myself as the first element
    #     # keep track of states -> path taken so far
    #     stack.append((start, [start]))
    #     result = []
    #     while stack:
    #         (curr, path) = stack.pop()
    #         # visited.add(curr)
    #         if curr == end:
    #             result.append(path) # successful path
    #             continue
    #         for neighbor in self.cables.get(curr, []):
    #             if neighbor not in path:
    #                 stack.append((neighbor, path + [neighbor]))

    #     return len(result)

    
    def part1(self, start='you', end='out'):
        return self.count_paths(start, end)
    
    def part2(self):
        # get number of paths going from svr -> fft -> dac -> out
        # and also number of paths going from svr -> dac -> fft -> out
        
        paths_fft_dac = self.count_paths('svr', 'fft') * self.count_paths('fft', 'dac') * self.count_paths('dac', 'out')
        paths_dac_fft = self.count_paths('svr', 'dac') * self.count_paths('dac', 'fft') * self.count_paths('fft', 'out')
        return paths_fft_dac + paths_dac_fft

def main():
    with open("11.txt") as f:
        doc = f.read()
    lines = doc.split('\n')
    cables = {}
    for line in lines:
        [device, output] = line.split(':')
        output = output.strip().split()
        cables[device] = output

    print(f"Part 1: {Day11(cables).part1()}")
    print(f"Part 2: {Day11(cables).part2()}")

    # print(cables) 

if __name__=="__main__":
    main()