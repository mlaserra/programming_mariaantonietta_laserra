def read_matrix(matrix_file):
    matrix = {}
    infile = open(matrix_file, "r")
    AA = infile.readline().split()[-1]
    n = 0
    for line in infile:
        line = line.split()
        for i in range(len(line)):
            matrix[AA[n]+AA[i]]= int(line[i][:-1])
            matrix[AA[i]+AA[n]]= int(line[i][:-1])
        n = n +1
    return matrix

print read_matrix("PAM250.txt")
print read_matrix("BLOSUM62.txt")
