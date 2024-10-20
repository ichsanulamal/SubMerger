#!/bin/bash

python vtt_dir2srt_dir.py "DIR" -r -e utf-8 
python srt_dir2md.py "DIR" out.md

