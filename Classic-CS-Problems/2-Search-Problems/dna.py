from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum("Nucleotide", ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]



def string_to_gene(s: str):
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene

# linear search
def linear_contains(gene: Gene, codon: Codon) -> bool:
    for c in gene:
        if c == codon:
            return True
    return False

# binary search
def binary_contains(gene: Gene, codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1 
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] > codon:
            high = mid - 1
        elif gene[mid] < codon:
            low = mid + 1
        else:
            return True
    return False



if __name__ == "__main__":
    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    my_gene: Gene = string_to_gene(gene_str)
    print(my_gene)

    my_sorted_gene: Gene = sorted(my_gene)
    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
    assert binary_contains(my_sorted_gene, acg) == True
    assert binary_contains(my_sorted_gene, gat) == False
