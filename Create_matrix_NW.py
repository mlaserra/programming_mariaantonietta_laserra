def build_matrix(s1,s2,d):
    score_matrix = []
    traceback_matrix = []
    m = len(s1)+1
    n = len(s2)+1
    #Zero matrix:
    for i in range(n):
        score_matrix.append([0]*m)
        traceback_matrix.append([0]*m)
    #update values of rows with penalties
    for p in range(1, m):
        score_matrix[0][p]= p * -d
        traceback_matrix[0][p] = "l"
    #update values of columns with penalties
    for q in range(1, n):
        score_matrix[q][0]= q *-d
        traceback_matrix[q][0] = "u"
    return score_matrix, traceback_matrix


print build_matrix("AAA","CC",2)

