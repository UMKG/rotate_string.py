#This program will concatenate segmented sequence lines in order and rewrite them into a single line in a fasta format file.
#Please specify the name of the input file and the name of the output file.
#This program does not work if there are multiple headers.

import sys
import argparse

#Create argument parser
parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-i', '--input_file', type=str, required=True, help='The input file name')
parser.add_argument('-o', '--output_file', type=str, required=True, help='The output file name')

# Parse arguments
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

#Check if there are more than two > in the input file
with open(input_file, 'r') as f:
    if f.read().count('>') >= 2:
        print("Error: The input file contains two or more '>' characters.")
        sys.exit(1)

with open(input_file, 'r') as f:
    lines = f.readlines()
    first_line = lines[0] # Get the first line
    new_sentence = ''.join(lines[1:]).replace('\n', '') # Get second and subsequent lines and concatenate them
    with open(output_file, 'w') as nf:
        nf.write(first_line + new_sentence) # Write first line and concatenated string

"""
Example

[before]
>seq1
abcd
efgh
ijkl

[after]
>seq1
abcdefghijk

"""
