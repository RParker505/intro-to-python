# Class stores a person's height in ft and in in two data attributes
class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    # Define less than < operator
    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B

    # Define less than or equal to <= operator
    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B

    # Define equal = operator
    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B

    # Define greater than > operator
    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

    # Define greater than or equal to >= operator
    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    # Define not equal to != operator
    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B

# Test the comparison operators, should all be True
print(Height(4, 5) < Height(4, 6))
print(Height(4, 5) <= Height(4, 5))
print(Height(5, 10) == Height(5, 10))
print(Height(4, 6) > Height(4, 5))
print(Height(4, 5) >= Height(4, 5))
print(Height(5, 9) != Height(5, 10))

# Test a few that should be False
print(Height(5, 10) == Height(4, 10))
print(Height(4, 6) > Height(5, 5))
print(Height(4, 5) >= Height(4, 6))