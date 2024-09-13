# Rotate_string.py (beta version)

This script performs circular permutation of single DNA sequence in a fasta format.

You can download the python script and run it from a terminal.

## Usage

If the sequence is segmented, concatenate them by using concate.py or another tool in advance.

### Circular permutation
For example, if gene X is from a-th to b-th, to make gene X the first, the argument should be set as ``-n a-th``.

``python rotate_string.py -i input_file_name -o output_file_name -n a-th``

### Complimentary revese circular permutation
If you want the complementary reversed sequence, add the argument ``-c``.

For example, if gene X is the a-th to b-th complementary strand, to make gene X the first, the argument should be set as
``-n b+1 -c``.

``python rotate_string.py -i input_file_name -o output_file_name -n b+1 -c``
