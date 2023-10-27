
# When creating seamless garments in 3d Software, a 2D pattern is used to wrap around the body.
# In order for tiled textures to seamlessly fit into the given pattern, the texture image must be able to divide into the pattern evenly.
# Given a choice of scaling the image up or down, this image resize calculator outputs a new width dimension that can be used in the 3D program

# importing use ceil and floor function to round up or down
import math

# Get input from the user for pattern width
while True:
    try:
        # Prompt the user to enter the width of the 2D garment pattern
        pattern_width = float(input("Enter the width of the 2D garment pattern:  "))
        # check if input is a negative float
        if pattern_width <= 0:
            raise ValueError("Invalid input. Please enter a positive number.")
        break
    # Handle the exception if the input is invalid and assign the error message to a variable to be able to change easily later
    except ValueError as e:
        print(e)

# Get input from the user for the image width
while True:
    try:
        # Prompt the user to enter the width of the image texture
        image_width = float(input("Enter the width of the image texture:  "))
        # Check if invalid input is negative float and is larger than the width of pattern
        if image_width > pattern_width or image_width < 0:
            raise ValueError("Invalid input. Please enter a positive number less than or equal to the pattern width.")
        break
    # assign the error message to a variable to be able to change easily later
    except ValueError as e:
        print(e)
# Divide pattern width by image width
result = pattern_width / image_width

# Get input from user if they want the image to get slightly bigger or smaller and loop condition set to prevent invalid input
while True:
    try:
        # Prompt the user to enter whether they want to scale the texture up or down
        rounding_method = input("Would you like to scale the texture (up or down):  ")
        if rounding_method == "up":
            # Round up the result using the ceil function from the math library
            rounded_result = math.ceil(result)
            break
        elif rounding_method == "down":
            # Round down the result using the floor function from the math library
            rounded_result = math.floor(result)
            break
        else:
            # Handle the exception if the input is invalid and assign the error message to a variable to be able to change easily later
            raise ValueError("Invalid! Your choice is 'up' or 'down'. Please enter your choice:")
    # assign the error message to a variable to be able to change easily later
    except ValueError as e:
        print(e)

# Divide pattern width by chosen rounded result by user
final_width = pattern_width / rounded_result
# Include only 6 decimal places for the final width
final_width = float(format(final_width, ".6f"))

# Display the final width of the image
print("The final width of the image should be:  ", final_width)

