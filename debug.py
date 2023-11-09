# Python program with 2 errors
# var = "Double value"
# sumvalue = var + 4

# Request a value from the user
def check_value(value_to_check):
    assert (type(value_to_check) is int), "You must enter a number."
    assert (value_to_check > 0), "Value entered must be greater than 0."
    if value_to_check > 4:
        print("Value is greater than 4.")


var = int(input("Enter a number greater than 0: "))

check_value(var)