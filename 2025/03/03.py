class Day3:
    def __init__(self, input_str: str):
        # split document into banks
        # convert banks (strings) into a list of integers
        self.banks = []
        banks = input_str.split('\n')
        for bank in banks:
            self.banks.append([int(batt) for batt in bank])
        

        # print(self.banks)
        

    def turn_on_1(self, bank: list):
        # must get largest first digit and largest digit after the original largest digit
        # the largest first digit is just the largest digit in the original string
        # then filter out all previous digits

        first_digit = max(bank[:-1])
        second_digit = max(bank[bank.index(first_digit)+1:])

        return first_digit * 10 + second_digit

    def turn_on_2(self, bank: list):
        # the largest 12-digit subsequence from the bank
        # so this is basically finding the largest digit that has at least 11 numbers following it
        # then finding the largest digit after the first digit that has at least 10 numbers following it, etc.
        # i guess we could turn it into a list of (value, distance from right)
        # then use prev values to constrain ranges
        output = ""
        l = 0
        # should have 11 numbers left 
        r = len(bank)-11
        for _ in range(12):
            max_digit = 0
            max_index = float('-inf')
            for i in range(l, r):
                curr_digit = bank[i]
                if curr_digit > max_digit:
                    max_digit = curr_digit
                    max_index = i
            output += str(max_digit)
            l = max_index+1
            r += 1

        return int(output)
        

        
                
    
    def part1(self):
        output = 0
        for bank in self.banks:
            joltage = self.turn_on_1(bank)
            # print(joltage)
            output += joltage

        return output
        
        # print(output)

    def part2(self):
        output = 0
        for bank in self.banks:
            joltage = self.turn_on_2(bank)
            # print(joltage)
            output += joltage

        return output

if __name__ == "__main__":
    with open("03.txt") as f:
        doc = f.read()
    
    print(f"Part 1: {Day3(doc).part1()}")
    print(f"Part 2: {Day3(doc).part2()}")