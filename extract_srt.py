import argparse
import re

def extract_text_from_srt(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding="utf8") as f:
        srt_contents = f.read()

    # Use regular expressions to extract the text only
    pattern = r'[0-9]+\n[0-9:,]+\s-->\s[0-9:,]+\n(.+?)\n\n'
    text_only = re.findall(pattern, srt_contents, re.DOTALL)

    # Join the list of text fragments into a single string
    text = ' '.join(text_only)

    with open(output_file_path, 'a', encoding="utf8") as f:
        f.write(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract text from an SRT file.')
    parser.add_argument('input_file', help='Path to the input SRT file.')
    parser.add_argument('output_file', help='Path to the output text file.')
    args = parser.parse_args()

    extract_text_from_srt(args.input_file, args.output_file)
