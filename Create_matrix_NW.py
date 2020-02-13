def build_matrix(s1,s2,matrix_file,d):
    score_matrix = []
    traceback_matrix = []
    m = len(s1)+1
    n = len(s2)+1
    #Zero matrix:
    for i in range(n):
        score_matrix.append([0]*m)
        traceback_matrix.append([0]*m)
    #update values of rows with penalties
    for c in range(1, m):
        score_matrix[0][c]= c * -d
        traceback_matrix[0][c] = "l"
    #update values of columns with penalties
    for r in range(1, n):
        score_matrix[r][0]= r *-d
        traceback_matrix[r][0] = "u"
     for r in range(1,n):
        for c in range(1,m):
            scores = {}
            up = 0
            letf = 0
            diag = 0
            up = score_matrix[r-1][c] + d
            letf = score_matrix[r][c-1] +d
            diag = score_matrix[r-1][c-1] + read_matrix(matrix_file)[s1[c-1]+s2[r-1]])
            final_score = max(up, diag, left)
            score_matrix[r][c]= final_score
    return score_matrix, traceback_matrix


seq1 = "GSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKL"
seq2 = "GNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKL"


print build_matrix(seq1,seq2,"BLOSUM62.txt", -2)

