# Subtitle to E-Book Converter

This is a command-line tool that converts subtitles in VTT or SRT format (directories or single text) to a single e-book in TXT or MD format. 

## Requirements

- Python 3.6 or higher
- webvtt (for VTT support)
- pysrt (for SRT support)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/subtitle-to-ebook.git
   cd subtitle-to-ebook
   ```

2. Install the dependencies:

   ```
   pip install webvtt pysrt
   ```

## Usage

```
1.
python dir_vtt.py input_directory output_file.md
Example:
python dir_srt.py "D:\D\Pagawean\video\Finance\SSCP Cert Prep - 3 Risk Identification, Monitoring, and Analysis (2021)" 2 risk.md 

2.
python dir_srt.py input_directory depth_of_directory output_file.md
Example:
python dir_vtt.py "D:\\D\\Pagawean\\video\\Cloud\\Coursera - Google IT Support Professional Certificate [Complete] [FCO]" output.md

3.
python extract_srt.py input_file.srt output_file.txt
Example:
python extract_srt.py inside.srt inside.txt

4.
python extract_vtt.py input_file.srt output_file.txt
Example:
python extract_vtt.py chomsky.vtt zizek.txt
```

5.
python extract_ttml.py input.ttml output.txt
Example:
python extract_ttml.py zp.ttml eekpeter.txt

## Supported Formats

This tool supports the following subtitle formats:

- VTT (WebVTT)
- SRT (SubRip)
- TTML (Timed Text Markup Language)

## Limitations

- This tool only supports subtitles in English.
- This tool does not support complex formatting or styling of subtitles.
- This tool may not work with non-standard or malformed subtitle files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## Acknowledgments

- Thanks to the authors of webvtt and pysrt for their excellent subtitle parsing libraries.


`

