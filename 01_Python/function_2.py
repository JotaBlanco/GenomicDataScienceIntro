"""
(2) What are the lengths of the sequences in the file?
What is the longest sequence and what is the shortest sequence?
Is there more than one longest or shortest sequence?
What are their identifiers?
"""
import pandas as pd

def analyse_seq_length(seq_dict):
    df = pd.DataFrame()
    for id_i in seq_dict:
        df_i = pd.DataFrame({"id": [id_i], "seq_length": [len(seq_dict[id_i])]})
        df = pd.concat([df, df_i])
    df = df.reset_index(drop=True)

    print("Lengths of the sequences in the file")
    print(df[["seq_length"]].describe())

    print("\n\nLongest sequence(s)")
    longest_seq = df["seq_length"].max()
    print(df[df["seq_length"]==longest_seq])
    print("Number of letters in seq:", longest_seq)
    print("Number of sequences with same number:", len(df[df["seq_length"]==longest_seq]))
    print("Ids:")
    for id_i in df.loc[df["seq_length"]==longest_seq,"id"]:
        print("-", id_i)

    print("\n\nShortest sequence(s)")
    shortest_seq = df["seq_length"].min()
    print(df[df["seq_length"] == shortest_seq])
    print("Number of letters in seq:", shortest_seq)
    print("Number of sequences with same number:", len(df[df["seq_length"] == shortest_seq]))
    print("Ids:")
    for id_i in df.loc[df["seq_length"] == shortest_seq, "id"]:
        print("-", id_i)
