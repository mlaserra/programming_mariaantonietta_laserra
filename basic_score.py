def score(seq1,seq2):
    score = 0
    if len(seq1)==len(seq2):
        for i in range(len(seq1)):
            if seq1[i]==seq2[i]:
                score = score +1
            else:
                score = score -1
        return score
    else:
        print "The sequences haven't the same length"

print "The sequence have a score of", score("ATA", "AAA")
