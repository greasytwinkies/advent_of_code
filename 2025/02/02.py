# an invalid ID only contains the same repeated sequence
# could be repeated an x number of times

# if you splice the string in half and compare them, they should be the same
# this only applies to strings of even length, so we can safely ignore strings of odd length 
class IDList:
    def __init__(self, input: str):
        self.ids = [tuple(map(int, rng.split("-"))) for rng in input.split(",")]
        # print(self.ids)
        self.invalid = []

    def is_invalid_1(self, id: int):
        id_str = str(id)
        n = len(id_str)
        return n % 2 == 0 and id_str[:n//2] == id_str[n//2:]
    
    def part1(self):
        for (start, end) in self.ids:
            for num in range(start, end+1):
                if self.is_invalid_1(num):
                    self.invalid.append(num)

        return sum(self.invalid)
    
    def is_invalid_2(self, id:int):
        # try all the factors of id len (except 1)
        # string of len f1 * f2 should return the same string
        id_str = str(id)
        n = len(id_str)
        for i in range(1, n):
            # i will be the length of the repeated string
            # first check that it is a factor
            if n % i != 0:
                continue
            else:
                # get number of times repeated
                if id_str[:i] * (n//i) == id_str:
                    return True
        
        return False
                    

    def part2(self):
        # sequence repeated at least twice
        for (start, end) in self.ids:
            for num in range(start, end+1):
                if self.is_invalid_2(num):
                    self.invalid.append(num)

        return sum(self.invalid)




if __name__ == "__main__":
    with open('02.txt') as f:
        doc = f.read()
    print(f"Part 1: {IDList(doc).part1()}")
    print(f"Part 2: {IDList(doc).part2()}")
