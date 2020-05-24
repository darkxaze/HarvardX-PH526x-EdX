inputfile = "dna.txt"
f = open(inputfile, "r")
seq = f.read()

seq = seq.replace("\n", "")
seq = seq.replace("\r", "") 

def translate(seq):
    """ Translate a string containing a nucleotide sequence into a 
    string containing the corresponding sequence of amino acids .
    Nucleotides are translated in triplets using the table dictionary; 
    each amino acid 4 is encoded with a string of length 1."""

    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}

    # check that the sequence length is divisible by 3
    # for each iteration of loop, extract single codoon
    # look up codon and store result
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i+6]
            protein += table[codon]
        return protein
    else:
        print("Key not found")

print(translate('TGGG'))
#print(help(translate))
#print(translate("GCC"))
#print(seq[40:50])