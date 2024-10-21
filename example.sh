#!/bin/bash

python vtt_dir2srt_dir.py "files" -r -e utf-8 
python srt_dir2md.py "files" out.md

python gptchunks.py