# brute force
# iterate over all red tiles
# calculate area with all other red tiles
import re

class Day9:
    def __init__(self, red_tiles: list):
        self.red_tiles = red_tiles
        # self.red_tiles.append(red_tiles[0])
        # max_cols = sorted(self.red_tiles, reverse=True)[0][0]+1
        # max_rows = sorted(self.red_tiles, reverse=True, key=lambda x : x[-1])[0][-1]+1
        # self.grid = [["." for _ in range(max_cols)] for _ in range(max_rows)]
        # for (c, r) in self.red_tiles: 
        #     self.grid[r][c] = "#"

        # print(*self.grid, sep='\n')

    def place_green_tiles(self):
        # connect each red tile with the tile after it
        pairs = list(zip(self.red_tiles, self.red_tiles[1:-1]))
        # print(pairs)
        for pair in pairs:
            (c1, r1) = pair[0]
            (c2, r2) = pair[-1]
            # print(r1,c1)
            # print(r2,c2)
            if r1 == r2:
                for i in range(min(c1, c2)+1, max(c1,c2)):
                    self.grid[r1][i] = "X"
            elif c1 == c2:
                for i in range(min(r1, r2)+1, max(r1,r2)):
                    self.grid[i][c1] = "X"
        
        grid_str = "\n".join("".join(row) for row in self.grid)

        def replace(match):
            s = match.group()       # the matched string
            return f"#" * len(s)    # replacement string depends on match length

        result = re.sub(r"(?<=[X#])\.+(?=[X#])", replace, grid_str)
        self.grid = [[char for char in line] for line in result.split('\n')]
        # print(*self.grid, sep='\n')
    
    def part1(self):
        max_area = float('-inf')
        # iterate over all red tiles
        for (r1, c1) in self.red_tiles:
            for (r2, c2) in self.red_tiles:
                area = abs(r1-r2+1) * abs(c1-c2+1)
                max_area = max(area, max_area)
        
        return max_area
    
    # def part2(self):
    #     # adjacent red tiles are connected by green tiles
    #     # list wraps, so last tile is connected to first and vice versa
    #     # area is filled with green tiles
    #     # get largest area made using only green or red tiles
    #     # rectangle must still have red tiles in opposite corners
    #     # so we must verify that all tiles in between are red or green? 
    #     # i guess we can simulate it with a grid
    #     self.place_green_tiles()
    #     # print(*self.grid, sep='\n')
    #     # now iterate over all the red tiles again, and then check that all tiles in between are red or green
    #     max_area = float('-inf')
    #     # iterate over all red tiles
    #     for (c1, r1) in self.red_tiles:
    #         for (c2, r2) in self.red_tiles:
    #             valid = True
    #             for r in range(min(r1,r2), max(r1,r2)+1):
    #                 for c in range(min(c1, c2), max(c1, c2)+1):
    #                     if self.grid[r][c] == ".":
    #                         valid = False
    #                         break
    #             if valid:
    #                 area = area = abs(r1-r2+1) * abs(c1-c2+1)
    #                 max_area = max(max_area, area)
            
        

    #     return max_area









def main():
    with open('09.txt') as f: 
        doc = f.read()
    red_tiles = [tuple(map(int, line.split(','))) for line in doc.split('\n')]

    print(f'Part 1: {Day9(red_tiles).part1()}')
    # print(f'Part 2: {Day9(red_tiles).part2()}')

    # print(red_tiles)

if __name__=="__main__":
    main()

