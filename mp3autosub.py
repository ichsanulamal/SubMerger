import os
from pydub import AudioSegment
import speech_recognition as sr

def mp3_to_wav(mp3_file):
    wav_file = mp3_file.replace('.mp3', '.wav')
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')
    return wav_file

def generate_subtitles(wav_file):
    recognizer = sr.Recognizer()
    subtitles = []

    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
        try:
            text = recognizer.recognize_google(audio_data)
            subtitles.append(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    return subtitles

def save_subtitles(subtitles, output_file):
    with open(output_file, 'w') as f:
        for line in subtitles:
            f.write(f"{line}\n")

def main(mp3_file):
    wav_file = mp3_to_wav(mp3_file)
    subtitles = generate_subtitles(wav_file)
    output_file = mp3_file.replace('.mp3', '.txt')
    save_subtitles(subtitles, output_file)
    
    # Clean up
    os.remove(wav_file)

if __name__ == "__main__":
    mp3_file = '/home/al/dwhelper/How to Angel Invest Part 1 - YouTube.mp3'  # Change this to your .mp3 file path
    main(mp3_file)
