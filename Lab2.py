def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input()

    temperature_list = []

    for value in user_input.split(","):
        temperature_list.append(float(value))

    return temperature_list


def calc_average_temperature(temperature_list):
    average = sum(temperature_list) / len(temperature_list)
    return average


def calc_min_max_temperature(temperature_list):
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)

    return [min_temp, max_temp]


def sort_temperature(temperature_list):
    return sorted(temperature_list)


def calc_median_temperature(temperature_list):
    sorted_list = sorted(temperature_list)

    n = len(sorted_list)

    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] +
                  sorted_list[n // 2]) / 2

    return median


def main():
    
    display_main_menu()

    temperatures = get_user_input()

    average = calc_average_temperature(temperatures)

    min_max = calc_min_max_temperature(temperatures)

    sorted_temperatures = sort_temperature(temperatures)

    median = calc_median_temperature(temperatures)

    print("\nResults")
    print("Average =", average)
    print("Minimum Temperature =", min_max[0])
    print("Maximum Temperature =", min_max[1])
    print("Sorted List =", sorted_temperatures)
    print("Median =", median)


if __name__ == "__main__":
    main()