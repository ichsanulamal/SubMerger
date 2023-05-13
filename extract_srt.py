import argparse
import re

def extract_text_from_srt(input_file_path):
    with open(input_file_path, 'r', encoding="utf8") as f:
        srt_contents = f.read()

    # Use regular expressions to extract the text only
    pattern = r'[0-9]+\n[0-9:,]+\s-->\s[0-9:,]+\n(.+?)\n\n'
    text_only = re.findall(pattern, srt_contents, re.DOTALL)

    # Join the list of text fragments into a single string
    text = ' '.join(text_only)

    output_file = input_file_path.replace(".srt", ".txt")
    with open(output_file, 'a', encoding="utf8") as f:
        f.write(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract text from an SRT file.')
    parser.add_argument('input_file', help='Path to the input SRT file.')
    args = parser.parse_args()

    extract_text_from_srt(args.input_file)
