try:
    import pandas  # Importing the pandas library

    a = 100  # Initializing variable a
    b = 1000  # Initializing variable b

    print(f'Variable a is set to: {a}')  # Printing value of a
    print(f'Variable b is set to: {b}')  # Printing value of b

    my_list = [2, 4, 6, 8]  # Creating a list
    print(f'The fourth element in the list is: {my_list[3]}')  # Printing the fourth element of the list

    print(f'The result of {a} divided by 1 is: {a / 1}')  # Performing division

except ModuleNotFoundError:
    print('Error: The required module could not be found. Please check the module you are importing.')  # Handling module not found error

except NameError:
    print('Error: A variable was referenced before assignment. Please check the defined variables.')  # Handling name error

except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')  # Handling division by zero error

except Exception as e:
    print(f'An unexpected error occurred: {e}')  # Handling any other exceptions

else:
    print('The code executed successfully without any errors.')  # Executed if no errors occur

finally:
    print('Execution complete. This block runs regardless of whether an error occurred.')  # Always executed

# Else statement will work when there is no error
# Finally statement will work in both cases
