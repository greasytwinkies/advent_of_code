from collections import deque
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

class Day7:
    def __init__(self, doc: str):
        # convert the grid into a 2D array with boundary padding
        self.grid = [["X", *list(line), "X"] for line in doc.split('\n')]
        # add top and bottom boundaries
        self.grid.insert(0, ["X"] * len(self.grid[0]))
        self.grid.append(["X"] * len(self.grid[0]))
        # find start position
        self.start = (1, self.grid[1].index("S"))

    def part1(self):
        char = lambda row, col: self.grid[row][col]
        q = deque([self.start])
        visited = set()

        while q:
            row, col = q.pop()
            curr = char(row, col)

            if curr in (".", "S"):
                q.append((row+1, col))
            elif curr == "^":
                if (row, col) not in visited:
                    q.append((row, col-1))
                    q.append((row, col+1))
                    visited.add((row, col))
            # else: 'X', terminate

        return len(visited)

    # part 2:
    # iterate over each row from top to bottom 
    # for each cell (col) in each row,
    # if current cell is empty cell, dump into next row same col
    # if current cell is a splitter, then dump it into r-1, c-1 and r-1, c+1
    # terminate if current cell == 0, cos that means there are no paths that pass through the current cell

    def part2(self):
        char = lambda row, col: self.grid[row][col]
        rows = len(self.grid)
        cols = len(self.grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[self.start[0]][self.start[-1]] = 1 

        # iterate over each row (account for padding)
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if dp[r][c] == 0: # no paths lead to this cell. terminate
                    continue
                # otherwise, there are paths that lead to this cell. check what the cell is
                curr = char(r, c)
                if curr == "." or curr == "S":
                    # should be moving downwards
                    dp[r+1][c] += dp[r][c]
                elif curr == "^": # if a splitter, then we should split down diagonally
                    dp[r+1][c-1] += dp[r][c]
                    dp[r+1][c+1] += dp[r][c]
        
        # we just need to return the sum of values in the last row
        return sum(dp[rows-2])

def main():
    with open("07.txt") as f:
        doc = f.read()

    day7 = Day7(doc)
    print(f"Part 1: {day7.part1()}")
    print(f"Part 2: {day7.part2()}")

if __name__ == "__main__":
    main()
