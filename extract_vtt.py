import argparse
import re
import webvtt

def extract_text(input_file, output_file):
    with open(output_file, 'w') as f:
        captions = webvtt.read(input_file)
        text = ' '.join(caption.text.strip() for caption in captions)
        text = re.sub(r'\n+', ' ', text)
        f.write(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input VTT file')
    parser.add_argument('output_file', help='Output TXT file')
    args = parser.parse_args()
    extract_text(args.input_file, args.output_file)
