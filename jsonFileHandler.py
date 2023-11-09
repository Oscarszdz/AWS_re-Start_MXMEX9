import json

# Defining the function that will read the file:
def read_json_file(filename):
    data = ""
    # Adding a try/expect block to make this function more reliable
    try:
        with open('files/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file.")
    return data