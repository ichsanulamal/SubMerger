import os
import re

def natural_sort_key(filename):
    # Split the filename into numbers and non-numeric parts
    return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', filename)]

def merge_txt_to_md():
    # Get a list of all .txt files in the current directory
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
    # Sort the files using the natural sort key
    txt_files.sort(key=natural_sort_key)

    # Specify the output .md file
    output_file = 'merged_output.md'

    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as md_file:
        for txt_file in txt_files:
            # Read the content of each .txt file
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()
                # Write the content to the .md file
                md_file.write(f"# {txt_file}\n\n")  # Adding the file name as a header
                md_file.write(content + "\n\n")     # Adding content and a new line

    print(f'Merged {len(txt_files)} files into {output_file}')

if __name__ == "__main__":
    merge_txt_to_md()
