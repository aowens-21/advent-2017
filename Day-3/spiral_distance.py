"""This is kind of a weird solution to understand(at least for me it was), hopefully the comments clarify how my solution works

    Used to find distance from center to destination on a spiral array like this:
      17   16   15   14    13
      18    5    4    3    12
      19    6    1    2    11
      20    7    8    9    10
      21   22   23   24    25

    For example, distance to 25 is 4 (right, right, down, down)
"""
def main():
    destination = int(input("Enter the number you'd like the distance to: "))
    print(compute_distance_to(destination))

def compute_distance_to(destination):
    #Our distance will start as 0
    distance = 0
    #The side of the length will be the lowest odd square < the destination number
    length_of_side = get_side_length(destination)
    #Midpoint of the side will be the start of that side + the square/2 (integer division)
    side_midpoint = compute_side_midpoint(destination, length_of_side)
    #Keep adding to distance until we reach the destination
    while (side_midpoint != destination):
        if (destination < side_midpoint):
            distance += 1
            side_midpoint -= 1
        else:
            distance += 1
            side_midpoint +=1
    #Final distance is the distance computed so far + the square/2 because we have to travel outward from center
    return distance + int(length_of_side/2)


def get_side_length(destination):
    #First odd square is 3
    square = 3
    while (square * square < destination):
        square += 2
    return square

#Returns middle of the side the number is located on
def compute_side_midpoint(destination, square):
    bottom_right_corner = square * square
    #1 is added here because we have to get the corner (not corner - 1)
    side_start = bottom_right_corner - square + 1
    while (destination < side_start):
        side_start = side_start - square + 1
    return side_start + int(square / 2)

main()