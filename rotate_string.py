'''
This script performs circular permutation of string (nucleotide sequence) in a fasta format.
If the nucleotide sequence is segmented, concatenat the sequence by using concate.py or another tool.
If you want the sequence to be complementary reversed, add the argument -c.
For example, if gene X is the a-th to b-th complementary strand, to make gene X the first, the argument should be set as
-n b+1 -c.
'''

import argparse

def circular_permutation(s: str, n: int, c:bool) -> str:
    if c:
        s = s.translate(str.maketrans('ATGC','TACG'))
        s = s[n-1:] + s[:n-1]
        #print(str(s))
        s = s[::-1]
        #print(str(s))
        return s
    return s[n-1:] + s[:n-1]
 
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Perform a circular permutation of a string.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file name')
    parser.add_argument('-o', '--output', type=str, required=True, help='Onput file name')
    parser.add_argument('-n', '--position', type=int, required=True, help='Position to start the circular permutation')
    parser.add_argument('-c', '--complement', action='store_true', help='Perform reverse complementation (optional)')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        lines = f.readlines()
        first_line = lines[0]
        s = lines[1].strip()

    result = circular_permutation(s, args.position, args.complement)

    output_file = args.output if args.output else args.input
    with open(output_file, 'w') as f:
        f.write(first_line + result)
