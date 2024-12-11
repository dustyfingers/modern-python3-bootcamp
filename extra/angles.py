import math

# write a function that, given a length and an angle of a vector, returns the coodrinate form of that vector
def coordinates_from_length_and_angle(length, angle):
    x_comp = length * math.cos(math.radians(angle))
    y_comp = length * math.sin(math.radians(angle))
    return [x_comp, y_comp]

# test cases
print(coordinates_from_length_and_angle(4, 165))
print(coordinates_from_length_and_angle(12, 235))