import re
import argparse
import chardet
from concurrent.futures import ProcessPoolExecutor

def read_file_chunk(file, chunk_size):
    while chunk := file.read(chunk_size):
        yield chunk

def count_tokens_chunk(chunk):
    # Try to detect the encoding of the data
    detected_encoding = chardet.detect(chunk)
    encoding = detected_encoding.get('encoding', 'utf-8')

    # Attempt to decode the data using the detected encoding
    try:
        text_data = chunk.decode(encoding)
    except:
        # Fallback to UTF-8 if decoding fails
        text_data = chunk.decode('utf-8', errors='replace')
        
    tokens = re.findall(r'\b\w+\b', text_data)
    return len(tokens)

def count_tokens(filename):
    chunk_size = 1024 * 1024  # 1 MB
    total_tokens = 0

    with open(filename, 'rb') as file:
        with ProcessPoolExecutor(max_workers=12) as executor:
            total_tokens = sum(executor.map(count_tokens_chunk, read_file_chunk(file, chunk_size)))

    return total_tokens

parser = argparse.ArgumentParser(description="Count the tokens in a file.")
parser.add_argument('filename', type=str, help="Path to the file.")

args = parser.parse_args()

print(f'The file {args.filename} contains {count_tokens(args.filename)} tokens.')
