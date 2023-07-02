import re

def split_paragraphs(text, words_per_paragraph=200):
    # Remove unwanted leading and trailing whitespace
    text = text.strip()

    # Replace newline characters with a space
    text = text.replace('\n', ' ')

    # Remove excess spaces between words
    text = re.sub(' +', ' ', text)

    # Split text into sentences using punctuation as delimiters
    sentences = re.split('(?<=[.!?])\s+', text)

    paragraphs = []
    current_paragraph = ''
    word_count = 0

    for sentence in sentences:
        words = sentence.split()


        for word in words:
            current_paragraph += word + ' '
            word_count += 1

            if word_count >= words_per_paragraph:
                paragraphs.append(current_paragraph.strip())
                current_paragraph = ''
                word_count = 0

    if current_paragraph:
        paragraphs.append(current_paragraph.strip())

    return '\n\n'.join(paragraphs)
