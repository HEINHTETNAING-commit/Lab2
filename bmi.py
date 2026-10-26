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