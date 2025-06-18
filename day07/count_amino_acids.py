import sys
from textwrap import wrap

codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}

aa_table = {}
for key, values in codon_table.items():
    for val in values:
        aa_table[val] = key

filename = sys.argv[1]
#Text name: ser_seq.txt

aa_count = {}
L=[]
converted_L = []
with open(filename, "r") as file:
    for line in file:
        line = line.rstrip("\n")
        L.append(line.upper())
    whole_seq = "".join(L)
    divided_seq = wrap(whole_seq, 3)
    for triplet in divided_seq:
        converted_L.append(aa_table[triplet])
    for aa in converted_L:
        if aa not in aa_count:
            aa_count[aa] = 1
        else:
            aa_count[aa] = aa_count[aa]+1

aa_count_sorted = sorted(aa_count)
for x in aa_count_sorted:
    print("{:<6}{}\n".format(x, aa_count[x]))
