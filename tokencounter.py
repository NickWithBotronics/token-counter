import re
import argparse
import chardet

def count_tokens(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        
    # Try to detect the encoding of the data
    detected_encoding = chardet.detect(data)
    encoding = detected_encoding.get('encoding', 'utf-8')

    # Attempt to decode the data using the detected encoding
    try:
        text_data = data.decode(encoding)
    except:
        # Fallback to UTF-8 if decoding fails
        text_data = data.decode('utf-8', errors='replace')
        
    tokens = re.findall(r'\b\w+\b', text_data)
    return len(tokens)

parser = argparse.ArgumentParser(description="Count the tokens in a file.")
parser.add_argument('filename', type=str, help="Path to the file.")

args = parser.parse_args()

print(f'The file {args.filename} contains {count_tokens(args.filename)} tokens.')
