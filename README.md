This script performs circular permutation of string in a fasta format.

If the sequence is segmented, concatenate them by using concate.py or another tool in advance.

For example, if gene X is from a-th to b-th, to make gene X the first, the argument should be set as
-n a-th.

Usage (via terminal)
>python rotate_string.py -i input_file -o output_file(required) -n a-th

If you want the complementary reversed sequence, add the argument -c.
For example, if gene X is the a-th to b-th complementary strand, to make gene X the first, the argument should be set as
-n b+1 -c.

Usage (via terminal)
>python rotate_string.py -i input_file -o output_file(required) -n b+1 -c
