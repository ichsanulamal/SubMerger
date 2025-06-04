#!/bin/bash

# python vtt_dir2srt_dir.py "files" -r -e utf-8 
uv run srt_dir2md.py "files" out.md
uv run gptchunks.py

find ./files -type f -name "*.srt" -exec rm -f {} \;
find ./files -type f -name "*.txt" -exec rm -f {} \;

find . -type f -name "chunk_*" -exec rm -f {} \;
