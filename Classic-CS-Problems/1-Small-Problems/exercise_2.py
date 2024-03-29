"""
You saw how the simple int type in Python can be used to represent a bit string. 
Write an ergonomic wrapper around int that can be used generically as a sequence of bits 
(make it iterable and implement __getitem__()). Reimplement CompressedGene, using the wrapper.
"""
from sys import getsizeof


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.bit_string = self._compress(gene)

    def __str__(self):
        return self.decompress()

    def __getitem__(self, key):
        if isinstance(key, slice):
            decompressed: str = self.decompress()
            parts = [decompressed[i:i+4] for i in range(0, len(decompressed), 4)]
            return parts[key.start:key.stop:key.step]
        elif isinstance(key, int):
            decompressed: str = self.decompress()
            key = (key * 4)
            if key < 0:
                key = len(decompressed) + key
            return decompressed[key:key+4]

    def _compress(self, gene: str) -> None:
        bit_string: int = 1  # start with sentinel
        for nucleotide in gene.upper():
            bit_string <<= 2  # shift left two bits
            if nucleotide == "A":  # change last two bits to 00
                bit_string |= 0b00
            elif nucleotide == "C":  # change last two bits to 01
                bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 10
                bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 11
                bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
        return bit_string
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude
        # sentinel
            bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # reverses string by slicing backward

    # def bytes_to_int(self, bytes_s: bytes) -> int:
    #     result = 0
    #     for b in bytes_s:
    #         result = result * 256 + int(b)
    #     return result

    # def _compress(self, gene: str) -> None:
    #     gene_bytes: bytes = gene.encode("utf-8")
    #     return self.bytes_to_int(gene_bytes)
    #     # self.bit_string = int.from_bytes(gene_bytes, "big")

    # def decompress(self) -> str:
    #     temp: bytes = self.bit_string.to_bytes((self.bit_string.bit_length()+ 7) // 8, "little")
    #     return temp.decode("utf-8")[::-1]

    # def _compress(self, gene: str) -> None:
    #     gene_bytes: bytes = gene.encode()
    #     self.bit_string = int.from_bytes(gene_bytes, "little")

    # def decompress(self) -> str:
    #     gene_bytes: bytes = self.bit_string.to_bytes(self.bit_string.bit_length(), "little")
    #     return gene_bytes.decode()




if __name__ == "__main__":
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))

    sequence: str = "TAGGGATTATGT"
    compressed: CompressedGene = CompressedGene(sequence)
    print(compressed[0])
    print(compressed[-1])
    print(compressed[-2])
    print(compressed[0:2])
    print(compressed[-2:-1])