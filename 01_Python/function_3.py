"""
(3) In molecular biology, a reading frame is a way of dividing the DNA sequence of nucleotides into a set of consecutive, non-overlapping triplets (or codons).
Depending on where we start, there are six possible reading frames: three in the forward (5' to 3') direction and three in the reverse (3' to 5').
For instance, the three possible forward reading frames for the sequence AGGTGACACCGCAAGCCTTATATTAGC are:

- AGG TGA CAC CGC AAG CCT TAT ATT AGC
- A GGT GAC ACC GCA AGC CTT ATA TTA GC
- AG GTG ACA CCG CAA GCC TTA TAT TAG C

These are called reading frames 1, 2, and 3 respectively. An open reading frame (ORF) is the part of a reading frame that has the potential to encode a protein.
It starts with a start codon (ATG), and ends with a stop codon (TAA, TAG or TGA). For instance, ATGAAATAG is an ORF of length 9.

Given an input reading frame on the forward strand (1, 2, or 3) your program should be able to identify all ORFs present
in each sequence of the FASTA file, and answer the following questions:

- what is the length of the longest ORF in the file?
- What is the identifier of the sequence containing the longest ORF?
- For a given sequence identifier, what is the longest ORF contained in the sequence represented by that identifier?
- What is the starting position of the longest ORF in the sequence that contains it?

The position should indicate the character number in the sequence. For instance, the following ORF in reading frame 1:
>sequence1 ATGCCCTAG starts at position 1.

Note that because the following sequence:
>sequence2 ATGAAAAAA does not have any stop codon in reading frame 1, we do not consider it to be an ORF in reading frame 1.
"""
import re
import pandas as pd

def analyse_seq_orfs(seq_dict):
    pattern = re.compile(r'(ATG.*?(TAA|TAG|TGA))')
    df = pd.DataFrame()

    for id_i in seq_dict:
        print("ID", id_i)
        seq_text = seq_dict[id_i]
        matches = [match[0] for match in pattern.findall(seq_text)]

        longest_orf = max(matches)
        start_position = seq_text.find(longest_orf)+1
        print("Longest ORF seq:", longest_orf)
        print("Starting position:", start_position)

        df_i = pd.DataFrame({
            "id": [id_i],
            "length_longest": [len(longest_orf)],
            "start_pos": [start_position]
        })
        df = pd.concat([df, df_i])

    df = df.reset_index(drop=True)
    longest_orf_ALL = df["length_longest"].max()
    print("\n\n\nLONGEST ORF from ALL SEQUENCES")
    print(df[df["length_longest"]==longest_orf_ALL])
