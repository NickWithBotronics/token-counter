import re
import argparse

def count_tokens(filename):
    with open(filename, 'r') as file:
        data = file.read()
        
    tokens = re.findall(r'\b\w+\b', data)
    return len(tokens)

parser = argparse.ArgumentParser(description="Count the tokens in a text file.")
parser.add_argument('filename', type=str, help="Path to the text file.")

args = parser.parse_args()

print(f'The file {args.filename} contains {count_tokens(args.filename)} tokens.')
