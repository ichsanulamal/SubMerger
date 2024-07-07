from vtt_to_srt.vtt_to_srt import ConvertDirectories

recursive = True
convert_file = ConvertDirectories("/home/al/Documents/courses/Artificial Intelligence AI for Trading - Udacity", recursive, "utf-8")
convert_file.convert()
    