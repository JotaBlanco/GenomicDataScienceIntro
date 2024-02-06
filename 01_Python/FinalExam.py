# READING FASTA FILE
# Open file
try:
    f = open("dna.example.fasta")
except IOError:
    print("File dna.example.data does not exist!")

# Iterate over lines
seqs = {}
for line in f:
    # let's discard the newline at the end (if any)
    line = line.rstrip()
    # distinguish header from sequence
    if line.startswith(">"):
        words = line.split()
        name = words[0][1:]
        seqs[name] = ""
    else: #sequence, not header
        seqs[name] = seqs[name] + line
f.close()

# Question 1
from function_1 import number_records_in_seq_dict
print("Qestion 1:", number_records_in_seq_dict(seqs))

# Question 2
from function_2 import analyse_seq_length
print("\n\n\nQUESTION 2")
analyse_seq_length(seqs)

# Question 3
from function_3 import analyse_seq_orfs
print("\n\n\nQUESTION 3")
analyse_seq_orfs(seqs)

# QUestion 4
from function_4 import find_repeats_in_all_seqs
print("\n\n\nQUESTION 4")
find_repeats_in_all_seqs(seqs, 10)
