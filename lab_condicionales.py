# Use input() function to get information from the user
user_reply = input("Do you need to ship a package? (Enter yes or no) ")

# Use the if statement to print a response
if user_reply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    


# Working with the elif statement
user_reply_2 = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if user_reply_2 == "stamps":
    print("We have many stamps designs to choose from.")
elif user_reply_2 == "envelope":
    print("We have many envelope sizes to choose from.")
elif user_reply_2 == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print(f"Here are {copies} copies")
else:
    print("Thank you, please come again!.")
