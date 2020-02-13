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
    return score_matrix, traceback_matrix


print build_matrix("AAA","CC",2)

