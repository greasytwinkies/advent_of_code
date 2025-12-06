# need to separate numbers by columns
# and then apply the operations
# we could do them line by line then transpose?
import math
import re

class Day6:
    def solve(self):
        grand_total = 0
        for i, col in enumerate(self.cols):
            # check operation type
            if self.operations[i] == "*":
                grand_total += math.prod(col)
            elif self.operations[i] == "+":
                grand_total += sum(col)
        
        return grand_total
    
class Day6_Part1(Day6):
    def __init__(self, doc: str):
        lines = doc.split('\n')
        # print(lines)
        cols, operations = [[int(num) for num in line.strip().split()] for line in lines[:-1]], lines[-1].split()
        # transpose numbers
        # print(numbers)
        cols = [list(row) for row in zip(*cols)]
        self.cols = cols
        self.operations = operations
        assert len(self.cols) == len(self.operations)
    
class Day6_Part2(Day6):
    SPANS_PATTERN = re.compile(r'[*+] +(?![*+])')
    def __init__(self, doc: str):
        # define a regex pattern on the operations row to preserve spacing and indices
        lines = doc.split('\n')
        operations = lines[-1]
        spans = [(m.start(0), m.end(0)) for m in re.finditer(self.SPANS_PATTERN, operations)]
        cols = []
        for (start, end) in spans:
            col = []
            for line in lines[:-1]:
                col.append(line[start:end])
        # print(spans)
            cols.append(col)
        # print(cols)
        # now we must transpose the elements in each col
        cols_transposed = [[int(''.join(tup).strip()) for tup in list(zip(*col))] for col in cols]
        self.cols = cols_transposed
        self.operations = operations.split()

        # print(self.operations)

def main():
    with open("06.txt") as f:
        doc = f.read()
    
    print(f"Part 1: {Day6_Part1(doc).solve()}")
    print(f"Part 2: {Day6_Part2(doc).solve()}")

if __name__=="__main__":
    main()
