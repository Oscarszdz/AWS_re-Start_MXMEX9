# Script to define how bananas I have.
user_bananas = int(input("How many bananas do you have? "))

if user_bananas >= 5:
    print("I have a large bunch of bananas!.")
elif user_bananas >= 1:
    print("I have a small bunch of bananas.")
else:
    print("I don't have any bananas.")