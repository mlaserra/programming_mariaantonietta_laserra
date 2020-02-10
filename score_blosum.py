seq1 ="ALASVLIRLITRLYP"
seq2 ="ASAVHLNRLITRLYP"
def score(seq1,seq2):
    blosum = {}
    blosum_file = open("blosum.txt","r")
#Create a list of AA:
#Take the first line
    AA = blosum_file.readline()
#Create a list of the characters of the sequences
    AA = AA.split()
    for line in blosum_file:
        string = line.split()
        for i in range(len(AA)):
            blosum[AA[i]+string[0]] = string[i+1]
    score = 0
    for i in range(len(seq1)):
        score = score + int(blosum[seq1[i]+seq2[i]])
    return score
    blosum_file.close()

print "The score of the sequences alignment with BLOSUM matrix is", score(seq1,seq2)

