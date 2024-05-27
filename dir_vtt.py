import argparse
import os
import webvtt
from snakemd import Document

def extract_transcript(vtt_file):
    vtt = webvtt.read(vtt_file)
    lines = []
    for line in vtt:
        lines.extend(line.text.strip().splitlines())

    transcript = ""
    previous = None
    for line in lines:
        if line != previous:
            transcript += " " + line
            previous = line

    return transcript.strip()

def convert_to_html(text):
    html = ""
    for line in text.split("\n"):
        html += "<div>" + line + "</div><br>"
    return html.strip()

def process_files(directory):
    doc = Document("Output")
    prev_category = ""
    for root, dirs, files in sorted(os.walk(directory)):
        for name in sorted(files):
            if name.endswith("en.vtt"):
                category = root.split('/')[-1]
                if category != prev_category:
                    doc.add_paragraph("<hr>")
                    doc.add_header(category, level=1)
                    prev_category = category

                title = os.path.splitext(name)[0].split("-")[0]
                doc.add_header(title, level=2)
                transcript = extract_transcript(os.path.join(root, name))
                doc.add_paragraph(transcript)

    return doc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process VTT files.')
    parser.add_argument('directory', help='The directory containing VTT files.')
    parser.add_argument('output_file', help='The output file for the generated document.')
    args = parser.parse_args()

    input_directory = args.directory
    output_file = args.output_file

    doc = process_files(input_directory)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(doc))
