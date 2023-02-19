from apriori import Apriori
import pandas as pd
import csv



def run_Apriori(dataset, minsup, minconf):
# # load Apriori model without selected_items
    ap = Apriori(dataset, minsup, minconf)

    # run algorithm
    ap.run()

    # print out frequent itemset
    ap.print_frequent_itemset()

    # print out rules
    ap.print_rule()

def get_data_from_input():
    input_array = []
    while True:
        # Prompt the user for input and store it as a string
        input_str = input("Enter a line of input (or type 'done' to finish): ")

        # If the user types 'done', break out of the loop and return the input array
        if input_str == "done":
            return input_array

        # Split the input string into words and store it as an array
        input_arr = input_str.split()

        # Add the input array to the larger input array
        input_array.append(input_arr)

def change_config():
    while True:
        try:
            # Prompt the user for input and convert it to a float
            min_support = float(
                input("Enter the minimum support value (between 0 and 1): "))
            min_confidence = float(
                input("Enter the minimum confidence value (between 0 and 1): "))
            # If either input is not within the range, raise an exception
            if min_support <= 0 or min_support >= 1 or min_confidence <= 0 or min_confidence >= 1:
                raise ValueError()

            # If both inputs are valid, return them
            return min_support, min_confidence
        except ValueError:
            # If either input is not a valid number or not within the range, print an error message and ask the user to try again
            print("Invalid input. Please enter values between 0 and 1 for both the minimum support and confidence.")

def option1():
    print("\n")
    dataset = get_data_from_input()
    global minsup, minconf
    while True:
        display_mini_menu()
        user_input = input("Enter the option number: ")
        if (user_input == "3"):
            break
        elif (user_input == "2"):
            option3()
        elif (user_input == "1"):
            print("!!! Apriori algorithm is running !!!")
            print("!!! Result: !!!")
            run_Apriori(dataset=dataset, minsup=minsup,minconf = minconf)
            input("Press anything to return to main menu!\n")
            break
        else:
            print("Invalid option. Please try again.\n")

def option2():
    print("\n")
    global minsup, minconf
    print("You chose option 2.")
    filepath = input("Enter the full path to the CSV file: ")
    try:
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
            print("Data read from", filepath, "and stored in dataset.")
    except IOError:
        print("Error: could not read file", filepath)
        return
    while True:
        display_mini_menu()
        user_input = input("Enter the option number: ")
        if user_input == "3":
            break
        elif user_input == "2":
            option3()
        elif user_input == "1":
            run_Apriori(dataset=dataset, minsup=minsup, minconf=minconf)
            input("Press anything to return to main menu!\n")
            break
        else:
            print("Invalid option. Please try again.\n")

def option3():
    print("\n")
    print("You are changing the program configuration ...")
    global minsup, minconf
    minsup, minconf = change_config()

# Define a function to display the menu options
def display_menu():
    print("|+++++++++++++++++++++++++++++++++++++++++++++++++|")
    print("|This is the current config:                      |")
    print("|\tMin support:    ", minsup, "                     |")
    print("|\tMin confidence: ", minconf, "                     |")
    print("|+++++++++++++++++++++++++++++++++++++++++++++++++|")
    print("Choose an option:")
    print("1. Option 1: Define dataset manually")
    print("2. Option 2: Import a .csv file for dataset")
    print("3. Option 3: Change config")
    print("or Type finished to end the program!")

# Define a function to display the mini menu options
def display_mini_menu():
    print("\n")
    print("Choose an option:")
    print("1.Start mining")
    print("2.Change config")
    print("3.Cancel")


# Define a dictionary that maps option numbers to functions
options = {
    "1": option1,
    "2": option2,
    "3": option3
}

# # set min support and min confidence
minsup = 0.2
minconf = 0.6


# Start the program
print("\n Welcome to the the Apriori Association Rule Miner!")

while True:
    # Display the menu and prompt for user input
    display_menu()
    user_input = input("Enter the option number: ")

    # If the user types 'finished', break out of the loop and end the program
    if user_input == "finished":
        print("Program ended.")
        break

    # If the user input is a valid option number, execute the corresponding function
    if user_input in options:
        options[user_input]()
    else:
        print("Invalid option. Please try again.\n")
