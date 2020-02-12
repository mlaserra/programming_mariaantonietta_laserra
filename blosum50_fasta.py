def blosum50_score(L):
    blosum50 = {'AA': 5, 'AR':-2, 'AN':-1, 'AD':-2, 'AC':-1, 'AQ':-1,'AE':-1,                   
                'AG': 0, 'AH':-2, 'AI':-1, 'AL':-2, 'AK':-1, 'AM':-1,'AF':-3,
                'AP':-1, 'AS': 1, 'AT': 0, 'AW':-3, 'AY':-2, 'AV': 0}
    score = 0
    if len(L) != 2:                                                                         #Check if we are aligning two sequences
        print "Error! More that two sequences"
     else:
        for i in range(len(L[0])):
            if len(L[0])==len(L[1]):                                                        #Check if the sequences have the same length
                if L[0][i]+L[1][i] in blosum50.keys():                                      #Check if the aligned residues are in the 
                    score = score + int(blosum50[L[0][i]+L[1][i]])                          #blosum50 dictionary and update the score value
    return score

def take_seq(fasta_file):
        sequences_file = open(fasta_file, "r")                                              #Open the fasta file and create an empty list
        sequences = []                                                                      #where to store the sequences to be aligned 
        for line in sequences_file:                                                             
            if not line.startswith('>'):
                line = line.strip()                                                         #Take the sequences and store them into the list
                sequences.append(line)                                                      #created before
        sequences_file.close()
        return sequences



print "The score for the two sequences using the blosum50 matrix is", blosum50_score(take_seq("hemoglobin.fasta"))      #Run the functions
