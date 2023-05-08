# Open the output file in write mode
with open("output.txt", "w") as outfile:
    # Iterate over the even numbers between 2 and 10000 (inclusive)
    for i in range(2, 10001, 2):
        # Write each even number to the file
        outfile.write(str(i) + "\n")
import os

def getOutputFile():
    while True:
        # Prompt the user for an output filename
        filename = input("Enter an output filename: ")
        # Check if the file already exists
        if os.path.isfile(filename):
            # If the file exists, ask the user if they want to overwrite it
            response = input("The file already exists. Overwrite? (y/n) ")
            if response.lower() == "y":
                # If the user confirms, return the filename
                return filename
        else:
            # If the file doesn't exist, return the filename
            return filename
# Open the output file in write mode
with open(getOutputFile(), "w") as outfile:
    # Iterate over the even numbers between 2 and 10000 (inclusive)
    for i in range(2, 10001, 2):
        # Write each even number to the file
        outfile.write(str(i) + "\n")
