import srt
import datetime
import sys
import ollama

# === CONFIG ===
OLLAMA_MODEL = 'llama3.2:1b'  # Change to your local model name


def load_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        subtitles = list(srt.parse(f.read()))
    return subtitles


def split_subtitles(subtitles, interval_minutes=15):
    parts = []
    current_part = []
    if not subtitles:
        return []

    start_time = subtitles[0].start
    end_time = start_time + datetime.timedelta(minutes=interval_minutes)

    for sub in subtitles:
        if sub.start >= end_time:
            parts.append(current_part)
            current_part = []
            start_time = sub.start
            end_time = start_time + datetime.timedelta(minutes=interval_minutes)
        current_part.append(sub)

    if current_part:
        parts.append(current_part)

    return parts


def summarize_with_ollama(content):
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                'role': 'user',
                'content': f"Summarize the following text:\n\n{content}",
            },
        ],
    )
    return response['message']['content'].strip()


def summarize_parts(parts):
    summaries = []
    for i, part in enumerate(parts):
        part_text = ' '.join(sub.content for sub in part)
        print(f"Summarizing part {i + 1} (length: {len(part_text)} chars)...")
        summary = summarize_with_ollama(part_text)
        summaries.append((i + 1, summary))
    return summaries


def main(srt_file_path):
    subtitles = load_srt(srt_file_path)
    parts = split_subtitles(subtitles, interval_minutes=15)
    summaries = summarize_parts(parts)

    print("\n=== Summaries ===")
    for idx, summary in summaries:
        print(f"\n--- Part {idx} ---\n{summary}\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python summarize_srt.py <your_subtitle_file.srt>")
        sys.exit(1)
    main(sys.argv[1])
