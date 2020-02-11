def blosum50_score(L):
    blosum50 = {'AA': 5, 'AR':-2, 'AN':-1, 'AD':-2, 'AC':-1, 'AQ':-1,'AE':-1,
                'AG': 0, 'AH':-2, 'AI':-1, 'AL':-2, 'AK':-1, 'AM':-1,'AF':-3,
                'AP':-1, 'AS': 1, 'AT': 0, 'AW':-3, 'AY':-2, 'AV': 0}
    score = 0
    if len(L) != 2:
        print "Error! More that two sequences"
     else:
        for i in range(len(L[0])):
            if len(L[0])==len(L[1]):
                if L[0][i]+L[1][i] in blosum50.keys():
                    score = score + int(blosum50[L[0][i]+L[1][i]])
    return score

def take_seq(fasta_file):
        sequences_file = open(fasta_file, "r")
        sequences = []
        for line in sequences_file:
            if not line.startswith('>'):
                line = line.strip()
                sequences.append(line)
        return sequences



print blosum50_score(take_seq("hemoglobin.fasta"))
