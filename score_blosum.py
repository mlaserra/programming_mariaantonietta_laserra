seq1 ="ALASVLIRLITRLYP"
seq2 ="ASAVHLNRLITRLYP"
def score(seq1,seq2):
    blosum = {}                                     #Create an empty dictionary for the pairs of the matrix
    blosum_file = open("blosum.txt","r")            # Read the matrix
    aminoacids = blosum_file.readline().split()     #Create a list of the aminoacids of the matrix
    for line in blosum_file:
        line = line.split()                       #Iterate for each line creating a list of the values associated to each pairs of AA
        for i in range(len(aminoacids)):                        #Iterate for all the AA filling the blosum dictionary
            blosum[aminoacids[i]+line[0]] = line[i+1]       
    score = 0
    for i in range(len(seq1)):
        if len(seq1)== len(seq2):
            score = score + int(blosum[seq1[i]+seq2[i]])            #Calculate the score for the aligned residues using the values
    return score                                                    #from blosum dictionary
    blosum_file.close()                                             #Close the file

print "The score of the sequences alignment with BLOSUM matrix is", score(seq1,seq2)

