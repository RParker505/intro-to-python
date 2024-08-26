# Class stores a person's height in ft and in in two data attributes
class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    # define method to print readable output when print is called
    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    # Used the __add__() method to define what happens when the + operator is invoked
    def __add__(self, other):
        # Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Adding them up
        total_height_inches = height_A_inches + height_B_inches

        # Getting the output in feet
        output_feet = total_height_inches // 12

        # Getting the output in inches
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

    # Use the __sub__() method to subtract feet and inches
    def __sub__(self, other):
        # Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Find the difference
        total_height_inches = height_A_inches - height_B_inches

        # Getting the output in feet
        output_feet = total_height_inches // 12

        # Getting the output in inches
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

# Initialize object for a single person's height
Adam = Height(5, 10)

print(Adam)

# Test the __add__ method
person_A_height = Height(5, 10)
person_B_height = Height(4, 10)
height_sum = person_A_height + person_B_height

print("Total height:", height_sum)

# Test the __sub__ method
person_C_height = Height(5, 10)
person_D_height = Height(3, 9)
height_diff = person_C_height - person_D_height 

print("Height difference:", height_diff)