"""
You saw how the simple int type in Python can be used to represent a bit string. 
Write an ergonomic wrapper around int that can be used generically as a sequence of bits 
(make it iterable and implement __getitem__()). Reimplement CompressedGene, using the wrapper.
"""
from sys import getsizeof


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def __str__(self):
        return self.decompress()

    def __getitem__(self, key):
        print(key)
        if isinstance(key, slice):
            start = key.start * 4 if key.start else None
            stop = key.stop * 4 if key.stop else None
            step = key.step * 4 if key.step else 1
            return self.decompress()[start:stop:step]
        elif isinstance(key, int):
            key = (key * 4)
            return self.decompress()[key:key+4]

    # def _compress(self, gene: str) -> None:
    #     self.bit_string: int = 1  # start with sentinel
    #     for nucleotide in gene.upper():
    #         self.bit_string <<= 2  # shift left two bits
    #         if nucleotide == "A":  # change last two bits to 00
    #             self.bit_string |= 0b00
    #         elif nucleotide == "C":  # change last two bits to 01
    #             self.bit_string |= 0b01
    #         elif nucleotide == "G":  # change last two bits to 10
    #             self.bit_string |= 0b10
    #         elif nucleotide == "T":  # change last two bits to 11
    #             self.bit_string |= 0b11
    #         else:
    #             raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
    
    def _compress(self, gene: str) -> None:
        gene_bytes: bytes = gene.encode("utf-8")
        self.bit_string = int.from_bytes(gene_bytes, "big")

    def decompress(self) -> str:
        temp: bytes = self.bit_string.to_bytes((self.bit_string.bit_length()+ 7) // 8, "big")
        return temp.decode("utf-8")

    # def _compress(self, gene: str) -> None:
    #     gene_bytes: bytes = gene.encode()
    #     self.bit_string = int.from_bytes(gene_bytes, "little")

    # def decompress(self) -> str:
    #     gene_bytes: bytes = self.bit_string.to_bytes(self.bit_string.bit_length(), "little")
    #     return gene_bytes.decode()

    # def decompress(self) -> str:
    #     gene: str = ""
    #     for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude
    #     # sentinel
    #         bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
    #         if bits == 0b00:  # A
    #             gene += "A"
    #         elif bits == 0b01:  # C
    #             gene += "C"
    #         elif bits == 0b10:  # G
    #             gene += "G"
    #         elif bits == 0b11:  # T
    #             gene += "T"
    #         else:
    #             raise ValueError("Invalid bits:{}".format(bits))
    #     return gene[::-1]  # [::-1] reverses string by slicing backward


if __name__ == "__main__":
    # original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)  # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))

    sequemce: str = "TAGGGATT"
    compressed: CompressedGene = CompressedGene(sequemce)
    print(compressed[:])