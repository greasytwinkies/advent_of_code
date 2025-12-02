# numbers range from 0 to 99
# left rotation -> towards lower numbers
# right rotation -> towards higher numbers

# turning dial leftwards from 0 returns 99
# similarly, turning dial rightwards from 99 returns 0

# dial starts pointing at 50

# actual password is the number of times the dial is pointing at 0 after any rotation in the sequence

class Dial:
    def __init__(self, document: str):
        self.password = 50
        self.instructions = document.split("\n")
        self.zero_count = 0

    def read_instruction(self, instruction: str):
        direction, magnitude = instruction[0], int(instruction[1:])
        return direction, magnitude

    def rotate_part1(self, direction: str, magnitude: int):
        if direction == "L":
            self.password = (self.password - magnitude) % 100
        else:
            self.password = (self.password + magnitude) % 100

    def rotate_part2(self, direction: str, magnitude: int):
        if direction == "L":
            for _ in range(magnitude):
                self.password -= 1
                self.password %= 100
                if self.password == 0:
                    self.zero_count += 1 
        else:
            for _ in range(magnitude):
                self.password += 1
                self.password %= 100
                if self.password == 0:
                    self.zero_count += 1 



    def part1(self):
        for instruction in self.instructions:
            d, m = self.read_instruction(instruction)
            self.rotate_part1(d, m)
            if self.password == 0:
                self.zero_count += 1
        return self.zero_count
    
    def part2(self):
        for instruction in self.instructions:
            d, m = self.read_instruction(instruction)
            self.rotate_part2(d, m)
            # print(self.password)
            # if self.password == 0:
            #     self.zero_count = 1
        return self.zero_count


if __name__ == "__main__":
    with open("01.txt") as f:
        doc = f.read()
    
    print(f"Part 1: {Dial(doc).part1()}")
    print(f"Part 2: {Dial(doc).part2()}")



