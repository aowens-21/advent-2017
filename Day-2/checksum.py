def main():
    with open('data/checksum.txt') as readFile:
        print(get_checksum(readFile))

def get_checksum(file):
    sum = 0
    for row in file:
        sum += get_difference_from_row(row)
    return sum

def get_difference_from_row(row):
    numbers = [int(num) for num in row.split('\t')]
    return max(numbers) - min(numbers)

main()