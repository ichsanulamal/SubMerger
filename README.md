# SubMerger

This is a command-line tool that converts subtitles in VTT or SRT or TTML format (directories or single text) to a single e-book in MD format. 

## Requirements

- webvtt (for VTT support)
- pysrt (for SRT support)

## Installation

1. Clone the repository:

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

```
1.
`python main.py <YOUR_FILE>`
```

### Directory

```
1.
python dir_vtt.py input_directory output_file.md

2.
python dir_srt.py input_directory output_file.md
```

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

