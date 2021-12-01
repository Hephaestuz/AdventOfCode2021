def read_file(file):
    with open(file, 'r') as f:
        for row in f:
            yield row.strip()

def part1(input_file):
    d = 0 # depth
    h = 0 # horizontal position
    for row in read_file(input_file):
        row = row.split()
        if row[0] == "forward":
            h += int(row[1])
        elif row[0] == "down":
            d += int(row[1])
        elif row[0] == "up":
            d -= int(row[1])
        else:
            raise Exception("Unexpected commands")
    print(d, h, d * h)

def part2(input_file):
    aim = 0
    d = 0
    h = 0
    for row in read_file(input_file):
        row = row.split()
        if row[0] == "forward":
            h += int(row[1])
            d += aim * int(row[1])
        elif row[0] == "down": 
            aim += int(row[1])
        elif row[0] == "up":
            aim -= int(row[1])
        else: 
            raise Exception("Unexpected command:", row[0], row)
    print(d, h, d * h)

if __name__ == "__main__":
    INPUT = 'input.txt'
    part1(INPUT)
    part2(INPUT)