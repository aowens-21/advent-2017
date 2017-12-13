def main():
    with open('data/checksum.txt') as readFile:
        print(get_evenly_divisible_number_sum(readFile))

def get_evenly_divisible_number_sum(file):
    sum = 0
    for row in file:
        sum += get_division_from_row(row)
    return sum

def get_division_from_row(row):
    numbers = [int(num) for num in row.split('\t')]
    for dividend in numbers:
        for divisor in numbers:
            if (dividend != divisor and dividend % divisor == 0):
                return int(dividend / divisor)

main()