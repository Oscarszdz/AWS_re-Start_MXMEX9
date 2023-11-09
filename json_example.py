import json

filename = 'user_name.json'
name = ''

# Check for a history file
try:
    with open(filename, 'r') as r:
        # Load the user's name from the history file
        name = json.load(r)
except IOError:
    print("First-time login")

# If the user was found in the history file, welcome them back
if name != "":
    print(f"Welcome back, {name}!")
else:
    # If the history file doesn't exists, as the user for their name
    name = input("Hello, what's your name? ")
    print(f"Welcome, {name}!")
    
    
# Save the user's name to the history file
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file.")