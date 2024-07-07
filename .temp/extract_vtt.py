import argparse
import re
import webvtt
from src.paragraph_splitter import split_paragraphs

def extract_text(input_file):
    output_file = input_file.replace(".vtt", ".txt")
    with open(output_file, 'w') as f:
        captions = webvtt.read(input_file)
        text = ' '.join(caption.text.strip() for caption in captions)
        text = re.sub(r'\n+', ' ', text)
        f.write(split_paragraphs(text))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input VTT file')
    args = parser.parse_args()
    extract_text(args.input_file)
