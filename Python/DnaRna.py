sequences =['ttgaaTgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg',
'gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau',
'gaaagcaagaaaaggcaggcgaggaagGgaagaagggggggaaacc',
'guuuccuacaguauuugaUgagaaugagaguuuacuccuggaagauaauauuagaauguuuacaacugcaccugaucagguggauaaggaagaugaagacu',
'gauaaggaagaugaagacuuucaggaaucuaauaaaaugcacuccaugaauggauucauguaugggaaucagccggguc']
'''for i in sequences:
    if ('t' or 'T') in i:
        print(i," is a sequence of DNA")
    elif ('u' or 'U') in i:
        print(i," is a sequence of RNA")
    else:
        print(i," is a sequence of unknown")'''
def dna_or_rna(list):
    for i in list:
        if ('t' or 'T') in i:
            print(i," is a sequence of DNA")
        elif ('u' or 'U') in i:
            print(i," is a sequence of RNA")
        else:
            print(i," is a sequence of unknown")
dna_or_rna(sequences)
sequences = ['GCCATTCTGC', 'GCTTACCCAA', 'CCTCTAGCGC', 'TAAATTTTGT',
'TGTGATACTG', 'AACAGAGCATCTCTTGTGACCAGTT', 
'TAGGCTGCCTGTGGCAGGTTGTTGCATTCTCTTAGAACCGCCCTGAACTC', 
'ATCCACAGACATCTCGTGTAAGGGG', 'CCCTCTTTCCAATTGACAGGATCAG']
def dna_complement(list):
    middle_sequence=[]
    complement_sequence=[]
    for i in list:
        if 'A' in i:
            #print(i.replace('A','T'))
            i=i.replace('A','m')
        if 'T' in i:
            #print(i.replace('T','A'))
            i=i.replace('T','n')
        if 'G' in i:
            #print(i.replace('G','C'))
            i=i.replace('G','o')
        if 'C' in i:
            #print(i.replace('C','G'))
            i=i.replace('C','p')
        middle_sequence.append(i)
    print(middle_sequence)
    for j in middle_sequence:
        if 'm' in j:
            #print(i.replace('A','T'))
            j=j.replace('m','T')
        if 'n' in j:
            #print(i.replace('T','A'))
            j=j.replace('n','A')
        if 'o' in j:
            #print(i.replace('G','C'))
            j=j.replace('o','C')
        if 'p' in j:
            #print(i.replace('C','G'))
            j=j.replace('p','G')
        complement_sequence.append(j)
    print(complement_sequence)
dna_complement(sequences)