def read_matrix(matrix_file):
    matrix = {}
    infile = open(matrix_file, "r")
    AA = infile.readline().split()
    for line in infile:
        line = line.split()
        for i in range(len(AA)):
            matrix[AA[i]+line[0]]= int(line[i+1])
            matrix[line[0]+AA[i]]= int(line[i+1])
    infile.close()
    return matrix

print read_matrix("blosum.txt")
