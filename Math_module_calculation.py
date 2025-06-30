# Importing math library to use maths calculation

import math

# Taking inpot from the user

number = float(input("Enter a number: "))

# Calculate and display the results

if number > 0:
    sqrt_result = math.sqrt(number)
    log_result = math.log(number)
else:
    sqrt_result = "Undefined (number must be non-negative)"
    log_result = "Undefined (number must be positive)"

sin_result = math.sin(number)

# Displaying the results

print("\nSquare root: ",sqrt_result)
print("Natural logarithm (log base e): ",log_result)
print("Sine (in radians): ",sin_result)
