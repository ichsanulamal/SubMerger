import os
import sys

def extract_ttml(directory, folder_name):
    # Create a list to store the contents of all TTML files
    ttml_contents = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".ttml"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                ttml_contents.append(file.read())

    # Write the combined contents into a single text file
    output_file = os.path.join(directory, folder_name + ".txt")
    with open(output_file, "w") as file:
        file.write("\n".join(ttml_contents))

    print("Extraction completed. Combined TTML file saved as:", output_file)

# Check if the directory path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the directory path as a command-line argument.")
    sys.exit(1)

# Extract the directory path from the command-line argument
directory_path = sys.argv[1]

# Check if the provided directory exists
if not os.path.isdir(directory_path):
    print("Invalid directory path.")
    sys.exit(1)

# Extract the folder name from the directory path
folder_name = os.path.basename(directory_path)

# Call the function to extract TTML files and save the combined file
extract_ttml(directory_path, folder_name)
