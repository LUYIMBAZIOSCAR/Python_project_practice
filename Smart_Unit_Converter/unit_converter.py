celsius_to_fahrenheit_factor=1.8
celsius_to_fahrenheit_offset=32
kilograms_to_pounds_factor=2.20462


def celsius_to_fahrenheit(value): 
    '''Convert celsius to fahrenheit'''
    return (value * celsius_to_fahrenheit_factor) + celsius_to_fahrenheit_offset


def kilograms_to_pounds(value):
    '''Convert from kilograms to pounds'''
    return (value*kilograms_to_pounds_factor)

def main():
    print("--Smart Unit Converter--")
    print("You can convert from:")
    print("1.Celsius to Fahrenheit")
    print('2.Kilograms to Pounds')

    user_choice=input('What conversion do you want?(1/2): ')
    
    try:
        user_value=int(input('Please enter the value you want to convert: '))
    except ValueError:
        print('Invalid number entered')

    if user_choice=='1':
        result=celsius_to_fahrenheit(user_value)
        print(f'{user_value}C = {result} F')
    elif user_choice=='2':
        result=kilograms_to_pounds(user_value)
        print(f'{user_value} kg = {result} pounds')
    else:
        print('Invalid conversion choice')

if __name__=="__main__":
    main()
    

