def read_fasta(fasta_file):
    sequences = []
    infile = open(fasta_file, "r")
    for line in infile:
        if not line.startswith('>'):
            line = line.strip()
            sequences.append(line)
    return sequences

print read_fasta("alignments.fasta")
