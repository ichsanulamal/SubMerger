import argparse
import os
import pysrt

def convert_srt_to_md(file_path, num_depth_of_dir):
    # Load the .srt file using pysrt
    subs = pysrt.open(file_path)

    # Build the Markdown output
    heading = " - ".join(file_path.split(os.path.sep)[(-1 * num_depth_of_dir) :]) 
    md_output = f"\n\n# {heading}\n\n"
    for sub in subs:
        # Split the subtitle into paragraphs by newlines and add each paragraph with a blank line between them
        for paragraph in sub.text.strip().split("\n"):
            md_output += f"{paragraph}" + " "

        # Add a blank line after each subtitle
        # md_output += " "

    # Return the Markdown output
    return md_output

def convert_all_srt_to_md(directory_path, num_depth_of_dir, output_file):
    # Recursively search for all .srt files in the directory
    srt_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".srt"):
                srt_files.append(os.path.join(root, file))

    # Convert each .srt file to Markdown and concatenate the output
    md_output = ""
    for srt_file in srt_files:
        md_output += convert_srt_to_md(srt_file, num_depth_of_dir) + "\n\n"

    # Save the output to a single .md file
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(md_output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert .srt files to Markdown.')
    parser.add_argument('directory', help='The directory containing .srt files.')
    parser.add_argument('num_depth_of_dir', type=int, help='Number of depth of directory for the heading.')
    parser.add_argument('output_file', help='The output file for the generated Markdown.')
    args = parser.parse_args()

    convert_all_srt_to_md(args.directory, args.num_depth_of_dir, args.output_file)
