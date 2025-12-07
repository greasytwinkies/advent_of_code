# # tachyon beams always move downward
# # starts from the manifold 'S'
# # if it encounters a splitter '^', then beam splits left and right and continues downward


# # DFS + keep track of visited splitters
# # return length of visited at the end
# # we can add an artificial terminating layer below the grid

# from collections import deque
# class Day7:
#     def __init__(self, doc: str):
#         # convert our grid into an array
#         # add some padding for OOB errors
#         self.grid = [["X", *list(line), "X"] for line in doc.split('\n')]
#         self.grid.append(["X" for _ in range(len(self.grid[0]))])
#         self.grid.insert(0, ["X" for _ in range(len(self.grid[0]))])
#         self.start = (1, self.grid[1].index('S'))
#         # print(*self.grid, sep='\n')
#         # print(self.start)

#     def part1(self):
#         char = lambda row, col : self.grid[row][col]
#         q = deque()
#         q.append(self.start)
#         visited = set()
#         while q:
#             (row, col) = q.pop()
#             curr = char(row, col)
#             if curr == "." or curr == "S":
#                 # continue vertically
#                 q.append((row+1,col))
#             elif curr == "^":
#                 # splitter, check if already visited
#                 if (row, col) not in visited:
#                     q.append((row, col-1))
#                     q.append((row, col+1))
#                     # add to visited
#                     visited.add((row, col))
#             else: # char is X, terminate
#                 pass
        
#         return len(visited)

#     def part2(self):
#         # we can start from the bottom of the grid up and then do a BFS starting from each end position
#         # for each end pos, find the number of ways to reach the starting point
#         # at each point (after the bottom layer, can go up, left or right depending on what is around)
#         char = lambda row, col : self.grid[row][col]
#         num_rows = len(self.grid)
#         num_cols = len(self.grid[0])
#         timelines = 0
#         # start from penultimate row (aka last row of original grid. don't touch l/r boundaries)
#         for col in range(1, num_cols-1):
#             print(col)
#             q = deque()
#             q.append((num_rows-2, col))
#             while q:
#                 # we can definitely go up
#                 (row, col) = q.pop()
#                 curr = char(row, col)
#                 if curr == ".":
#                     q.append((row-1, col))
#                 # check if there are adjacent splitters
#                     if self.grid[row][col-1] == "^":
#                         q.append((row-1, col-1))
#                     if self.grid[row][col+1] == "^":
#                         q.append((row-1, col+1))
#                 elif curr == "S":
#                     # we managed to reach the end, so this is a valid timeline
#                     timelines += 1
#                 else: # boundary reached OR hit a splitter (which is not theoretically possible), do nothing
#                     pass
#         return timelines
    

# def main():
#     with open(f'07.txt') as f:
#         doc = f.read()

#     print(f'Part 1: {Day7(doc).part1()}')
#     print(f'Part 2: {Day7(doc).part2()}')

# if __name__=="__main__":
#     main()

from collections import deque
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

# ---------- Helper for Part 2 (must be top-level for multiprocessing) ----------
def explore_from_col(grid, start_row, start_col):
    """
    BFS from a single column in the bottom row up to the start 'S'.
    Returns the number of timelines reaching 'S' from this column.
    """
    char = lambda r, c: grid[r][c]
    q = deque()
    q.append((start_row, start_col))
    timelines = 0

    while q:
        row, col = q.pop()
        curr = char(row, col)

        if curr == ".":
            q.append((row-1, col))
            # check for adjacent splitters
            if grid[row][col-1] == "^":
                q.append((row-1, col-1))
            if grid[row][col+1] == "^":
                q.append((row-1, col+1))
        elif curr == "S":
            timelines += 1
        # else: 'X' or splitter visited incorrectly, ignore
    return timelines

# ---------- Day7 Class ----------
class Day7:
    def __init__(self, doc: str):
        # convert the grid into a 2D array with boundary padding
        self.grid = [["X", *list(line), "X"] for line in doc.split('\n')]
        # add top and bottom boundaries
        self.grid.insert(0, ["X"] * len(self.grid[0]))
        self.grid.append(["X"] * len(self.grid[0]))
        # find start position
        self.start = (1, self.grid[1].index("S"))

    # ---------- Part 1 ----------
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


    def part2(self):
        num_rows = len(self.grid)
        num_cols = len(self.grid[0])
        bottom_row = num_rows - 2  # last real row

        with ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(explore_from_col, self.grid, bottom_row, col)
                for col in range(1, num_cols - 1)
            ]

            timelines = 0
            # Wrap as_completed with tqdm for progress
            for f in tqdm(as_completed(futures), total=len(futures), desc="Columns processed"):
                timelines += f.result()

        return timelines


# ---------- Main ----------
def main():
    with open("07.txt") as f:
        doc = f.read()

    day7 = Day7(doc)
    print(f"Part 1: {day7.part1()}")
    print(f"Part 2: {day7.part2()}")

if __name__ == "__main__":
    main()
