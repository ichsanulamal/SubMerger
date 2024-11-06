def chunk_text_file(input_file, chunk_size=10000):
    """
    Splits a text file into smaller chunks.

    :param input_file: The path to the input text file.
    :param chunk_size: The maximum size of each chunk (default is 4000 characters).
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into chunks
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    # Save each chunk to a new file
    for index, chunk in enumerate(chunks):
        output_file = f'chunk_{index + 1}.txt'
        with open(output_file, 'w', encoding='utf-8') as chunk_file:
            chunk_file.write(chunk)
        print(f'Saved {output_file}')

if __name__ == "__main__":
    input_path = 'out.md'  # Replace with your input file path
    chunk_text_file(input_path)
