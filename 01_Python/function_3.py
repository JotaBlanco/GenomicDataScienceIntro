"""
(3) In molecular biology, a reading frame is a way of dividing the DNA sequence of nucleotides into a set of consecutive, non-overlapping triplets (or codons).
Depending on where we start, there are six possible reading frames: three in the forward (5' to 3') direction and three in the reverse (3' to 5').
For instance, the three possible forward reading frames for the sequence AGGTGACACCGCAAGCCTTATATTAGC are:

- AGG TGA CAC CGC AAG CCT TAT ATT AGC
- A GGT GAC ACC GCA AGC CTT ATA TTA GC
- AG GTG ACA CCG CAA GCC TTA TAT TAG C

These are called reading frames 1, 2, and 3 respectively.

An open reading frame (ORF) is the part of a reading frame that has the potential to encode a protein.
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


def get_orfs_from_seq_text(seq_text, reading_frame):

    reading_frames_dict = {1: 0, 2: 2, 3: 1}
    start = reading_frames_dict[reading_frame]
    end = (len(seq_text) - start) // 3 * 3

    in_orf = False
    orfs_dict = {}

    for i in range(start, end, 3):
        codon_i = seq_text[i: i + 3]

        if in_orf is False:
            if codon_i == "ATG":
                current_orf = "ATG"
                index = i +1
                in_orf = True
            else:
                continue
        else:
            current_orf = current_orf + codon_i
            if codon_i in ["TAA", "TAG", "TGA"]:
                orfs_dict[(len(current_orf), index)] = current_orf
                in_orf = False

    return orfs_dict


def analyse_seq_orfs(seq_dict):
    all_frame_1 = {}
    all_frame_2 = {}
    all_frame_3 = {}

    for id_i in seq_dict:
        print("\nID", id_i)
        seq_text = seq_dict[id_i]

        dic_frame_1 = get_orfs_from_seq_text(seq_text, reading_frame=1)
        all_frame_1.update(dic_frame_1)
        print("Reading frame 1", sorted(dic_frame_1.keys(),reverse=True))

        dic_frame_2 = get_orfs_from_seq_text(seq_text, reading_frame=2)
        all_frame_2.update(dic_frame_2)
        print("Reading frame 2", sorted(dic_frame_2.keys(),reverse=True))

        dic_frame_3 = get_orfs_from_seq_text(seq_text, reading_frame=3)
        all_frame_3.update(dic_frame_3)
        print("Reading frame 3", sorted(dic_frame_3.keys(),reverse=True))

    print("\n\nReading frame 1")
    print(sorted(all_frame_1.keys(),reverse=True))
    print("\nReading frame 2")
    print(sorted(all_frame_2.keys(),reverse=True))
    print("\nReading frame 3")
    print(sorted(all_frame_3.keys(),reverse=True))

    print("\nALL Reading frames")
    all_frames = {}
    all_frames.update(all_frame_1)
    all_frames.update(all_frame_2)
    all_frames.update(all_frame_3)
    print(sorted(all_frames.keys(),reverse=True))

