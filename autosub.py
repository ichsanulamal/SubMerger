import os
import whisper
from pathlib import Path
import ffmpeg
from googletrans import Translator

def extract_audio(video_path, output_audio_path):
    """Extracts audio from a video file."""
    ffmpeg.input(video_path).output(output_audio_path, acodec="mp3", ac=1, ar="16k").run(overwrite_output=True)

def transcribe_and_translate(audio_path, model, translator):
    """Transcribes audio and translates text to English."""
    result = model.transcribe(audio_path)
    translated_segments = []
    for segment in result["segments"]:
        translated_text = translator.translate(segment["text"], src="auto", dest="en").text
        translated_segments.append({**segment, "text": translated_text})
    return translated_segments

def write_srt(segments, output_path):
    """Writes segments to an SRT file."""
    with open(output_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(segments, start=1):
            start_time = segment['start']
            end_time = segment['end']
            text = segment['text']

            start_time_str = format_timestamp(start_time)
            end_time_str = format_timestamp(end_time)

            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_time_str} --> {end_time_str}\n")
            srt_file.write(f"{text}\n\n")

def format_timestamp(seconds):
    """Formats timestamp in SRT time format (HH:MM:SS,ms)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{milliseconds:03}"

def process_videos(input_dir, output_dir, model):
    """Processes all video files in the directory and its subdirectories."""
    translator = Translator()
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.mp4', '.mkv', '.avi', '.mov')):
                video_path = os.path.join(root, file)
                audio_path = os.path.join(output_dir, Path(file).stem + ".mp3")
                srt_path = os.path.join(output_dir, Path(file).stem + ".srt")

                print(f"Processing: {video_path}")

                # Extract audio from video
                extract_audio(video_path, audio_path)

                # Transcribe and translate audio
                segments = transcribe_and_translate(audio_path, model, translator)

                # Write SRT file
                write_srt(segments, srt_path)

                # Clean up temporary audio file
                os.remove(audio_path)

                print(f"Subtitle saved: {srt_path}")

if __name__ == "__main__":
    input_directory = "."  # Change to your input directory
    output_directory = "output_subtitles"  # Change to your output directory

    os.makedirs(output_directory, exist_ok=True)

    whisper_model = whisper.load_model("medium")

    process_videos(input_directory, output_directory, whisper_model)
