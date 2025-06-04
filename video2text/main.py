import os
import subprocess
import whisper
import torch

def extract_audio(mkv_path, output_dir):
    """
    Extract audio from .mkv file using FFmpeg
    
    :param mkv_path: Path to .mkv file
    :param output_dir: Directory to save audio file
    :return: Path to extracted audio file
    """
    # Generate output audio filename
    audio_filename = os.path.splitext(os.path.basename(mkv_path))[0] + ".wav"
    audio_path = os.path.join(output_dir, audio_filename)
    
    # FFmpeg command to extract audio
    command = [
        "ffmpeg", 
        "-i", mkv_path,      # Input file
        "-vn",               # No video
        "-acodec", "pcm_s16le", # Audio codec
        "-ar", "16000",      # Audio sample rate (good for speech recognition)
        "-ac", "1",          # Mono audio
        audio_path           # Output file
    ]
    
    try:
        # Run FFmpeg command
        subprocess.run(command, check=True, stderr=subprocess.PIPE)
        return audio_path
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio from {mkv_path}: {e}")
        return None

def transcribe_mkv_files(input_path, output_dir=None):
    """
    Transcribe audio from .mkv files in directory and subdirectories
    
    :param input_path: Directory containing .mkv files
    :param output_dir: Directory to save transcripts and audio files
    """
    # Use default output directory if not specified
    if output_dir is None:
        output_dir = input_path
    
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    audio_dir = os.path.join(output_dir, "audio")
    transcript_dir = os.path.join(output_dir, "transcripts")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(transcript_dir, exist_ok=True)
    
    # Load Whisper model
    model = whisper.load_model("small")
    
    # Walk through directory recursively
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith(".mkv"):
                mkv_path = os.path.join(root, file)
                
                # Extract audio
                audio_path = extract_audio(mkv_path, audio_dir)
                
                if audio_path:
                    try:
                        # Transcribe audio
                        print(f"Transcribing: {mkv_path}")
                        result = model.transcribe(audio_path, language="id")
                        
                        # Generate transcript filename
                        transcript_filename = os.path.splitext(file)[0] + "_transcript.txt"
                        transcript_path = os.path.join(transcript_dir, transcript_filename)
                        
                        # Write transcription
                        with open(transcript_path, "w", encoding="utf-8") as f:
                            f.write(result["text"])
                        
                        print(f"Transcript saved to: {transcript_path}")
                        
                    except Exception as e:
                        print(f"Transcription error for {mkv_path}: {e}")

def main():
    # Get input directory
    input_directory = input("Enter directory with .mkv files: ")
    
    # Optional output directory
    output_directory = input("Enter output directory (Enter for same location): ") or None
    
    # Check GPU availability
    if torch.cuda.is_available():
        print("CUDA detected. Using GPU acceleration.")
    else:
        print("Using CPU. Transcription may be slower.")
    
    # Run transcription process
    transcribe_mkv_files(input_directory, output_directory)

if __name__ == "__main__":
    main()
