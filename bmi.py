def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    if bmi<18.5:
        print("Under weight")
    elif 18.5<bmi<25.0:
        print("Normal weight")
    else:
        print("Over weight")


    # Display BMI
    print("BMI =", bmi)

calculate_bmi(weight=57, height=1.73)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    # Read input from user
    user_input = input()

    # Split string into a list
    temp_list = user_input.split(",")

    # Convert strings to floats
    float_list = []
    for item in temp_list:
        float_list.append(float(item))

    # Return list of floats
    return float_list

def calc_average_temperature(temperature_list):
    average = sum(temperature_list) / len(temperature_list)
    return average
def calc_min_max_temperature(temperature_list):
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)

    return [min_temp, max_temp]
def calc_median_temperature(temperature_list):
    # Sort list in ascending order
    temperature_list.sort()

    n = len(temperature_list)

    # Odd number of elements
    if n % 2 == 1:
        median = temperature_list[n // 2]

    # Even number of elements
    else:
        median = (temperature_list[n // 2 - 1] +
                  temperature_list[n // 2]) / 2

    return median