import math
f = open('TGFB1_gene_popset_39766314.txt', 'r') # read fasta format sequence file
fileReadLine = f.readlines()                    # read lines of file
dictonary_seq = {}                              #intialization of dictonary variable for seq and its name
seq_name = ''                                   #intialization of variable
seq = ''                                        #intialization of variable
detected = 0
for element in fileReadLine:
    if element[0] == '>':
        if detected == 1:
            seq_name = seq_name.replace('\n','')
            seq = seq.replace('\n','')
            dictonary_seq[seq_name] = seq
            seq_name = ''
            seq = ''
            seq_name = element
            detected = 1
        else:
            seq_name = element
            detected = 1
    
    else:
        seq = seq +element

dictonary_seq[seq_name] = seq

#del dictonary_seq['']

seqlist = dictonary_seq.values()
chromosome_len = len(seqlist)
seq_len = len(seqlist[0])

# Calculations
Pie = 0 # intialization of variable
Num_of_SNP = 0 #intialization of variable
for i in range(0,seq_len):
    n = len(seqlist)
    counterA = 0
    counterG = 0
    counterC = 0
    counterT = 0
    for seq in seqlist:
        if seq[i] == 'A':
            counterA = counterA+1
        elif seq[i] == 'G':
            counterG = counterG+1
        elif seq[i] == 'C':
            counterC = counterC+1
        elif seq[i] == 'T':
            counterT = counterT+1
        elif seq[i] == 'N':
            counterA = counterA+1
            counterG = counterG+1
            counterC = counterC+1
            counterT = counterT+1
        else:
            n = n-1
    if (n != counterA) | (n != counterG) | (n != counterC) | (n != counterT):
        Herterzygosity_i = (n/(n-1))*(1 -(math.pow(counterA/n,2) + math.pow(counterG/n,2)  + math.pow(counterC/n,2) + math.pow(counterT/n,2)))
        Pie = Pie + Herterzygosity_i
        Num_of_SNP = Num_of_SNP + 1

# display result on screen
print : 'Number of SNPs are : ' + str(Num_of_SNP)
print : 'Number of Chromosomes are : ' + str(chromosome_len)
print : 'Length of the sequences are : ' + str(seq_len)
print : 'Value of pie is : ' + str(Pie)