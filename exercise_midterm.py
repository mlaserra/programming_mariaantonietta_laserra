def read_matrix(matrix_file):
    matrix = {}
    infile = open(matrix_file,"r")
    AA = infile.readline().split()[-1]
    n = 0
    for line in infile:
        line = line.split()
        for i in range(len(line)):
            matrix[AA[n]+AA[i]]=int(line[i][:-1])
            matrix[AA[i]+AA[n]]=int(line[i][:-1])
        n = n +1
    infile.close()
    return matrix

def read_fasta(fasta_file):
    sequences = []
    infile = open(fasta_file, "r")
    for line in infile:
        if not line.startswith('>'):
            line = line.rstrip()
            sequences.append(line)
    return sequences

def scoring(L,matrix_file):
    gap = -2
    score_list = []
    for j in range(0,len(L),2):
        if len(L[j])==len(L[j+1]):
            score = 0
            for i in range(len(L[j])):
                if '-' in L[j][i] or '-' in L[j+1][i]:
                    score = score + gap
                else:
                    score = score + int(read_matrix(matrix_file)[L[j][i]+L[j+1][i]])
        score_list.append(score)
    return score_list
    
    print "First alignment (BLOSUM): \n", scoring(read_fasta("alignments.fasta"),"BLOSUM62.txt")[0], "\n", "First alignment (PAM): \n", scoring(read_fasta("alignments.fasta
"),"PAM250.txt")[0], "\n", "Second alignment (BLOSUM): \n", scoring(read_fasta("alignments.fasta"),"BLOSUM62.txt")[1], "\n", "Second alignment (PAM): \n", scoring(read_
fasta("alignments.fasta"),"PAM250.txt")[1], "\n", "Third alignment (BLOSUM): \n", scoring(read_fasta("alignments.fasta"),"BLOSUM62.txt")[2], "\n", "Third alignment (PAM
): \n", scoring(read_fasta("alignments.fasta"),"PAM250.txt")[2]
