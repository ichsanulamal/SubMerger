import argparse
from vtt_to_srt.vtt_to_srt import ConvertDirectories

def main():
    parser = argparse.ArgumentParser(description="Convert VTT files to SRT format.")
    parser.add_argument("directory", type=str, help="Path to the directory containing VTT files.")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively search through directories.")
    parser.add_argument("-e", "--encoding", type=str, default="utf-8", help="Encoding for the output files. Default is 'utf-8'.")

    args = parser.parse_args()

    convert_file = ConvertDirectories(args.directory, args.recursive, args.encoding)
    convert_file.convert()

if __name__ == "__main__":
    main()

