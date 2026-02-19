# constants for unit conversion
celsius_to_fahrenheit_factor=1.8
celsius_to_fahrenheit_offset=32
kilograms_to_pounds_factor=2.20462


def celsius_to_fahrenheit(value): 
    '''Convert celsius to fahrenheit
    param value: Temperature in Celsius
    return: Temperature in Fahrenheit
    '''
    return (value * celsius_to_fahrenheit_factor) + celsius_to_fahrenheit_offset


def kilograms_to_pounds(value):
    '''Convert weight from kilograms to pounds
    param value: Weight in kilograms
    return: Weight in pounds
    '''
    return (value*kilograms_to_pounds_factor)

def main():
    '''This is the main function that controls the program flow
    Handles user interaction, input validation and output
    '''
    # Display title and conversion options
    print("--Smart Unit Converter--")
    print("You can convert from:")
    print("1.Celsius to Fahrenheit")
    print('2.Kilograms to Pounds')

    # Take in user choice and remove leading white space
    user_choice=input('What conversion do you want?(1/2): ').strip()
    
    # The try/except prevents the program from crashing when
    # the user enters a value that is not a number
    try:
        # The float() converts the string value to a float
        user_value=float(input('Please enter the value you want to convert: '))
    except ValueError:
        # This is triggered when the user enters a non-numeric input
        print('Invalid number entered')

     # Performing the selected conversion
    if user_choice=='1':
        result=celsius_to_fahrenheit(user_value)
        print(f'{user_value}C = {result} F')
    elif user_choice=='2':
        result=kilograms_to_pounds(user_value)
        print(f'{user_value} kg = {result} pounds')
    else:
        # Handling invalid selection of user choice
        print('Invalid conversion choice')

# This ensures the program only runs when executed directly
# and not when imported as a module in another script
if __name__=="__main__":
    main()
    

