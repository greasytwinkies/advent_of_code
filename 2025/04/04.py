# cannot have more than 4 rolls in 8 adjacent positions (up down left right diag.)
# we should probably add a boundary of empty cells to mitigate OOR errors
# then just iterate over the grid, looking for @s and checking whether they are valid

class Day4:
    def __init__(self, grid: str):
        # add padding - horizontally and vertically
        self.grid = [["."] + list(row) + ["."] for row in grid.split('\n')]
        new_len = len(self.grid[0])
        buffer = ["." for _ in range(new_len)]
        self.grid.insert(0, buffer)
        self.grid.append(buffer)
        # print(*self.grid, sep='\n')

    def is_accessible(self, row: int, col: int):
        # get number of adjacent rolls
        # just extract the 3x3 grid and minus the current col (this function assumes that the index is already a roll by default)
        count = -1
        for r in range(-1,2):
            for c in range(-1,2):
                if self.grid[row+r][col+c] == "@":
                    count += 1
        
        return count < 4
    
    def part1(self):
        accessible_list = []
        for r_idx, row in enumerate(self.grid):
            for c_idx, col in enumerate(row):
                if col == "@" and self.is_accessible(r_idx, c_idx):
                    accessible_list.append((r_idx, c_idx))
        # for (r, c) in accessible_list:
        #     self.grid[r][c] = "x"
        # print(*self.grid, sep='\n')
        return len(accessible_list)
    
    def part2(self):
        # modify the list after each round
        # terminate when accessible_list is empty (nothing can be accessed)
        rolls = 0
        while True:
            accessible_list = []
            for r_idx, row in enumerate(self.grid):
                for c_idx, col in enumerate(row):
                    if col == "@" and self.is_accessible(r_idx, c_idx):
                        accessible_list.append((r_idx, c_idx))
            if not accessible_list:
                return rolls
            else:
                rolls += len(accessible_list)
            for (r, c) in accessible_list:
                self.grid[r][c] = "."

if __name__=="__main__":
    with open("04.txt") as f:
        doc = f.read()
    print(f"Part 1: {Day4(doc).part1()}")
    print(f"Part 1: {Day4(doc).part2()}")


