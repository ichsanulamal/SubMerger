import os
import sys

def execute_if_txt(file_name):
    if file_name.endswith(".srt"):
        os.system("python extract_srt.py " + file_name)
    elif file_name.endswith(".vtt"):
        os.system("python extract_vtt.py " + file_name)
    elif file_name.endswith(".ttml"):
        os.system("python extract_ttml.py " + file_name)
    else:
        print("File type not supported.")
        return
    
    print('Done! Check the input folder for the output file.') 

def main():
    # Check if a file name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a file name.")
        return

    file_name = sys.argv[1]
    execute_if_txt(file_name)

if __name__ == "__main__":
    main()
