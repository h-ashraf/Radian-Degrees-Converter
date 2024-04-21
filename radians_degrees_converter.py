import math

def radians_to_degrees(radians):
    # Use the formula: degrees = radians * 180 / pi
    degrees = radians * 180 / math.pi
    return degrees

def degrees_to_radians(degrees):
    # Use the formula: radians = degrees * pi / 180
    radians = degrees * math.pi / 180
    return radians

def main():
    conversion_choice = input("Enter '1' to convert from radians to degrees or '2' to convert from degrees to radians: ")

    if conversion_choice == '1':
        radians_input = float(input("Enter the angle in radians: "))
        degrees_output = radians_to_degrees(radians_input)
        print(f"{radians_input} radians is equal to {degrees_output} degrees.")
    elif conversion_choice == '2':
        degrees_input = float(input("Enter the angle in degrees: "))
        radians_output = degrees_to_radians(degrees_input)
        print(f"{degrees_input} degrees is equal to {radians_output} radians.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
