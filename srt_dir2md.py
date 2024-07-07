import argparse
import os
import pysrt

import os
import pysrt

def srt_to_markdown(start_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as md_file:
        for root, dirs, files in os.walk(start_path):
            dirs.sort()  
            level = root.replace(start_path, '').count(os.sep)
            indent = '#' * (level + 1)
            
            if root != start_path:
                md_file.write(f"{indent} {os.path.basename(root)}\n\n")
            
            for file in sorted(files):
                if file.endswith('.srt'):
                    srt_path = os.path.join(root, file)
                    srt_content = pysrt.open(srt_path)
                    
                    file_name = os.path.splitext(file)[0]
                    md_file.write(f"{indent}# {file_name}\n\n")

                    out_text = ""
                    
                    for i, subtitle in enumerate(srt_content):
                        sbt_text = subtitle.text.replace('\n', ' ')
                        if i == len(srt_content) - 1:
                            out_text += f"{sbt_text}\n\n"
                        else:
                            out_text += f"{sbt_text} "
                    
                    md_file.write(out_text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert .srt files to Markdown.')
    parser.add_argument('directory', help='The directory containing .srt files.')
    parser.add_argument('output_file', help='The output file for the generated Markdown.')
    args = parser.parse_args()

    srt_to_markdown(args.directory, args.output_file)
