# FUNCTIONS FOR CUBE

# asks user for input and converts it into an integer
def get_side_length():
    user_input = int(input("Bitte geben Sie die Seitenlänge des Würfels ein: "))
    return user_input

# calculates the volume of a cube
def calculate_cube_volume(side_length):
    result = side_length ** 3
    return result


# FUNCTIONS FOR STEPCOUNTER

# asks user for distance and converts it into an integer, returns distance in cm
def get_distance():
    user_input = int(input("Bitte geben Sie die Entfernung in Zentimetern (cm) ein: "))
    return user_input

# asks user for step length and converts it into an integer, returns step length in cm
def get_step_length():
    user_input = int(input("Bitte geben Sie Ihre Schrittlänge in Zentimetern (cm) ein: "))
    return user_input

# calculates the number of steps for a given distance and step length, returns number of steps
def calculate_steps(distance, step_length):
    steps = distance / step_length
    return steps


# GENERAL FUNCTIONS

# prints result
def print_result(result):
    print(result)

