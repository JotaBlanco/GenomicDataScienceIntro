"""
(4) A repeat is a substring of a DNA sequence that occurs in multiple copies (more than one) somewhere in the sequence.
Although repeats can occur on both the forward and reverse strands of the DNA sequence, we will only consider repeats on the forward strand here.
Also we will allow repeats to overlap themselves. For example, the sequence ACACA contains two copies of the sequence ACA
- once at position 1 (index 0 in Python), and once at position 3.

Given a length n, your program should be able to identify all repeats of length n in all sequences in the FASTA file.
Your program should also determine how many times each repeat occurs in the file, and which is the most frequent repeat of a given length.
"""

def find_overlapping_repeats(sequence, n):
    repeats = {}
    for i in range(len(sequence) - n + 1):
        substring = sequence[i:i+n]
        repeats[substring] = repeats.get(substring, 0) + 1
    return repeats

def find_repeats_in_all_seqs(seq_dic, n):
    all_sequences = ""
    for id_i in seq_dic:
        all_sequences = all_sequences + seq_dic[id_i]

    repeats = find_overlapping_repeats(all_sequences, n)
    repeats_sorted = {k: v for k, v in sorted(repeats.items(), key=lambda item: item[1], reverse=True) if v>1}
    # print("REPEATS")
    # print(repeats)
    print("MOST FREQUENT REPEATS")
    print(repeats_sorted)
