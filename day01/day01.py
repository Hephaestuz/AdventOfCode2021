
import math

def read_file(file):
    with open(file, 'r') as f:
        for row in f:
            yield int(row.strip())

def part1():
    count = 0
    last = math.inf
    for row in read_file('input.txt'):
        if row > last:
            count +=1 
        last = row
    print(count)

def part2():
    group_length = 3 
    count = 0
    sums = [0] * group_length

    f = read_file('input.txt')

    for i, row in enumerate(f):
        for j in range(i+1):
            sums[j] += row
        i += 1
        if not i < group_length:
            break

    for row in f:
        sum = sums.pop(0)
        sums.append(0)
        for j in range(group_length):
            sums[j] += row
        if sums[0] > sum:
            count += 1
        
    print(count)

if __name__ == "__main__":
    part1()
    part2()